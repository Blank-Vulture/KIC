<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$pageTitle = "服用記録";
include 'header.php';
include 'db_config.php';

// 現在ログイン中のユーザーIDを取得
$stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
$stmt->bind_param("s", $_SESSION['user']);
$stmt->execute();
$stmt->bind_result($user_id);
$stmt->fetch();
$stmt->close();

// 服用記録の処理
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $medication_id = $_POST['medication_id'];
    $quantity = $_POST['quantity'];

    // 在庫数を減らす
    $stmt = $conn->prepare("UPDATE medications SET quantity = quantity - ? WHERE id = ? AND user_id = ?");
    $stmt->bind_param("iii", $quantity, $medication_id, $user_id);

    if ($stmt->execute()) {
        // 服用記録を追加
        $stmt = $conn->prepare("INSERT INTO medication_logs (medication_id, quantity) VALUES (?, ?)");
        $stmt->bind_param("ii", $medication_id, $quantity);

        if ($stmt->execute()) {
            echo "<div class='alert alert-success'>服用記録が追加されました！</div>";
        } else {
            echo "<div class='alert alert-danger'>服用記録の追加に失敗しました。</div>";
        }
        $stmt->close();
    } else {
        echo "<div class='alert alert-danger'>在庫の更新に失敗しました。</div>";
    }
}

// 薬品一覧を取得
$stmt = $conn->prepare("SELECT id, trade_name, quantity FROM medications WHERE user_id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$result = $stmt->get_result();
?>
<h2>服用記録</h2>
<form method="post" class="mt-4">
    <div class="mb-3">
        <label for="medication_id" class="form-label">薬品</label>
        <select name="medication_id" id="medication_id" class="form-select" required>
            <?php while ($row = $result->fetch_assoc()): ?>
                <option value="<?= $row['id'] ?>"><?= htmlspecialchars($row['trade_name']) ?> (残: <?= $row['quantity'] ?>)</option>
            <?php endwhile; ?>
        </select>
    </div>
    <div class="mb-3">
        <label for="quantity" class="form-label">服用数</label>
        <input type="number" name="quantity" id="quantity" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-primary">記録</button>
</form>
<a href="dashboard.php" class="btn btn-secondary mt-3">戻る</a>
<?php include 'footer.php'; ?>