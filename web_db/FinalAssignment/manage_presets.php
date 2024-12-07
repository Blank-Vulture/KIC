<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$pageTitle = "プリセット管理";
include 'header.php';
include 'db_config.php';

// 現在ログイン中のユーザーIDを取得
$stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
$stmt->bind_param("s", $_SESSION['user']);
$stmt->execute();
$stmt->bind_result($user_id);
$stmt->fetch();
$stmt->close();

// プリセットの作成処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['create_preset'])) {
    $preset_name = $_POST['preset_name'];

    $stmt = $conn->prepare("INSERT INTO presets (user_id, name) VALUES (?, ?)");
    $stmt->bind_param("is", $user_id, $preset_name);

    if ($stmt->execute()) {
        echo "<div class='alert alert-success'>プリセットが作成されました！</div>";
    } else {
        echo "<div class='alert alert-danger'>プリセットの作成に失敗しました。</div>";
    }
    $stmt->close();
}

// プリセットの削除処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['delete_preset'])) {
    $preset_id = $_POST['preset_id'];

    $stmt = $conn->prepare("DELETE FROM presets WHERE id = ? AND user_id = ?");
    $stmt->bind_param("ii", $preset_id, $user_id);

    if ($stmt->execute()) {
        echo "<div class='alert alert-success'>プリセットが削除されました！</div>";
    } else {
        echo "<div class='alert alert-danger'>プリセットの削除に失敗しました。</div>";
    }
    $stmt->close();
}

// プリセット一覧を取得
$stmt = $conn->prepare("SELECT id, name FROM presets WHERE user_id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$presets = $stmt->get_result();
?>
<h2>プリセット管理</h2>

<!-- 新規プリセット作成フォーム -->
<form method="post" class="mt-4">
    <div class="mb-3">
        <label for="preset_name" class="form-label">新規プリセット名</label>
        <input type="text" name="preset_name" id="preset_name" class="form-control" required>
    </div>
    <button type="submit" name="create_preset" class="btn btn-primary">プリセット作成</button>
</form>

<!-- 既存プリセット一覧 -->
<h3 class="mt-4">既存プリセット</h3>
<table class="table table-striped">
    <thead>
        <tr>
            <th>プリセット名</th>
            <th>操作</th>
        </tr>
    </thead>
    <tbody>
        <?php while ($preset = $presets->fetch_assoc()): ?>
        <tr>
            <td><?= htmlspecialchars($preset['name']) ?></td>
            <td>
                <a href="edit_preset.php?preset_id=<?= $preset['id'] ?>" class="btn btn-secondary btn-sm">編集</a>
                <form method="post" style="display:inline;">
                    <input type="hidden" name="preset_id" value="<?= $preset['id'] ?>">
                    <button type="submit" name="delete_preset" class="btn btn-danger btn-sm">削除</button>
                </form>
            </td>
        </tr>
        <?php endwhile; ?>
    </tbody>
</table>
<a href="dashboard.php" class="btn btn-secondary mt-3">戻る</a>
<?php include 'footer.php'; ?>