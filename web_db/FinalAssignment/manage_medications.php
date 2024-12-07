<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$pageTitle = "薬品管理";
include 'header.php';
include 'db_config.php';

// 現在ログイン中のユーザーIDを取得
$stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
$stmt->bind_param("s", $_SESSION['user']);
$stmt->execute();
$stmt->bind_result($user_id);
$stmt->fetch();
$stmt->close();

// 在庫数増加処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['add_stock'])) {
    $medication_id = $_POST['medication_id'];
    $additional_quantity = $_POST['additional_quantity'];

    $stmt = $conn->prepare("UPDATE medications SET quantity = quantity + ? WHERE id = ? AND user_id = ?");
    $stmt->bind_param("iii", $additional_quantity, $medication_id, $user_id);

    if ($stmt->execute()) {
        $success_message = "在庫が更新されました！";
    } else {
        $error_message = "在庫更新に失敗しました。";
    }
}

// ユーザーの薬品一覧を取得
$stmt = $conn->prepare("SELECT id, trade_name, quantity FROM medications WHERE user_id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$medications = $stmt->get_result();
?>

<h1 class="mt-4">薬品管理</h1>

<!-- 成功メッセージ -->
<?php if (isset($success_message)): ?>
<div class="alert alert-success"><?= htmlspecialchars($success_message) ?></div>
<?php endif; ?>

<!-- エラーメッセージ -->
<?php if (isset($error_message)): ?>
<div class="alert alert-danger"><?= htmlspecialchars($error_message) ?></div>
<?php endif; ?>

<table class="table table-striped mt-4">
    <thead>
        <tr>
            <th>薬品名</th>
            <th>残量</th>
            <th>在庫追加</th>
            <th>操作</th>
        </tr>
    </thead>
    <tbody>
        <?php while ($medication = $medications->fetch_assoc()): ?>
        <tr>
            <td><?= htmlspecialchars($medication['trade_name']) ?></td>
            <td><?= htmlspecialchars($medication['quantity']) ?></td>
            <td>
                <!-- 在庫追加フォーム -->
                <form method="post" style="display:flex; align-items: center;">
                    <input type="hidden" name="medication_id" value="<?= $medication['id'] ?>">
                    <input type="number" name="additional_quantity" class="form-control" placeholder="追加数" style="width: 100px; margin-right: 10px;" required>
                    <button type="submit" name="add_stock" class="btn btn-primary btn-sm">追加</button>
                </form>
            </td>
            <td>
                <!-- 薬品削除フォーム -->
                <form method="post" action="delete_medication.php" style="display:inline;">
                    <input type="hidden" name="medication_id" value="<?= $medication['id'] ?>">
                    <button type="submit" class="btn btn-danger btn-sm">削除</button>
                </form>
            </td>
        </tr>
        <?php endwhile; ?>
    </tbody>
</table>

<a href="add_medication.php" class="btn btn-primary mt-4">薬品を追加</a>

<?php include 'footer.php'; ?>