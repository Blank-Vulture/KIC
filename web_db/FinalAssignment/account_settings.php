<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$pageTitle = "アカウント情報編集";
include 'header.php';
include 'db_config.php';

// 現在ログイン中のユーザー情報を取得
$stmt = $conn->prepare("SELECT id, username FROM users WHERE username = ?");
$stmt->bind_param("s", $_SESSION['user']);
$stmt->execute();
$stmt->bind_result($user_id, $current_username);
$stmt->fetch();
$stmt->close();

// アカウント名変更処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['change_name'])) {
    $new_name = $_POST['new_name'];

    // アカウント名の変更
    $stmt = $conn->prepare("UPDATE users SET username = ? WHERE id = ?");
    $stmt->bind_param("si", $new_name, $user_id);

    if ($stmt->execute()) {
        $_SESSION['user'] = $new_name; // セッションを更新
        $success_message = "アカウント名が変更されました！";
    } else {
        $error_message = "アカウント名の変更に失敗しました。";
    }
}

// 服用履歴全削除処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['delete_logs'])) {
    $stmt = $conn->prepare("DELETE FROM medication_logs WHERE medication_id IN (SELECT id FROM medications WHERE user_id = ?)");
    $stmt->bind_param("i", $user_id);

    if ($stmt->execute()) {
        $success_message = "服用履歴が全て削除されました。";
    } else {
        $error_message = "服用履歴の削除に失敗しました。";
    }
}

// アカウント削除処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['delete_account'])) {
    $username_confirmation = $_POST['username_confirmation'];

    // 入力されたアカウント名と現在のデータベースの名前を比較
    if ($username_confirmation !== $current_username) {
        $error_message = "アカウント名が一致しません。";
    } else {
        // トランザクションを開始
        $conn->begin_transaction();

        try {
            // 関連データの削除
            $stmt = $conn->prepare("DELETE FROM medication_logs WHERE medication_id IN (SELECT id FROM medications WHERE user_id = ?)");
            $stmt->bind_param("i", $user_id);
            $stmt->execute();

            $stmt = $conn->prepare("DELETE FROM medications WHERE user_id = ?");
            $stmt->bind_param("i", $user_id);
            $stmt->execute();

            // ユーザーの削除
            $stmt = $conn->prepare("DELETE FROM users WHERE id = ?");
            $stmt->bind_param("i", $user_id);
            $stmt->execute();

            // トランザクションをコミット
            $conn->commit();
            session_destroy();
            header("Location: index.php");
            exit();
        } catch (Exception $e) {
            // トランザクションをロールバック
            $conn->rollback();
            $error_message = "アカウント削除に失敗しました: " . $e->getMessage();
        }
    }
}
?>

<h1 class="mt-4">アカウント情報編集</h1>

<!-- 成功メッセージ -->
<?php if (isset($success_message)): ?>
<div class="alert alert-success"><?= htmlspecialchars($success_message) ?></div>
<?php endif; ?>

<!-- エラーメッセージ -->
<?php if (isset($error_message)): ?>
<div class="alert alert-danger"><?= htmlspecialchars($error_message) ?></div>
<?php endif; ?>

<!-- アカウント名変更フォーム -->
<h2 class="mt-4">アカウント名変更</h2>
<form method="post">
    <div class="mb-3">
        <label for="new_name" class="form-label">新しいアカウント名</label>
        <input type="text" name="new_name" id="new_name" class="form-control" placeholder="新しいアカウント名を入力" required>
    </div>
    <button type="submit" name="change_name" class="btn btn-primary">変更</button>
</form>

<!-- 服用履歴全削除フォーム -->
<h2 class="mt-5">服用履歴全削除</h2>
<form method="post">
    <div class="mb-3">
        <p>この操作を実行すると、全ての服用履歴が削除されます。この操作は取り消せません。</p>
    </div>
    <button type="submit" name="delete_logs" class="btn btn-warning">服用履歴を全削除</button>
</form>

<!-- アカウント削除ボタン -->
<h2 class="mt-5">アカウント削除</h2>
<button id="deleteAccountButton" class="btn btn-danger">アカウント削除</button>

<!-- カスタムモーダルウィンドウ -->
<div id="deleteModal" class="custom-modal hidden">
    <div class="custom-modal-content">
        <span class="close-button" id="closeModal">&times;</span>
        <h2>アカウント削除確認</h2>
        <p>本当にアカウントを削除しますか？以下にアカウント名を入力してください:</p>
        <form method="post">
            <input type="text" name="username_confirmation" class="form-control" placeholder="アカウント名を入力" required>
            <div class="mt-3">
                <button type="submit" name="delete_account" class="btn btn-danger">削除</button>
                <button type="button" id="cancelDelete" class="btn btn-secondary">キャンセル</button>
            </div>
        </form>
    </div>
</div>

<?php include 'footer.php'; ?>