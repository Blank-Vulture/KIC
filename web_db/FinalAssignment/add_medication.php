<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$pageTitle = "薬品登録";
include 'header.php';
include 'db_config.php';

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $trade_name = $_POST['trade_name'];
    $quantity = $_POST['quantity'];

    // 現在ログイン中のユーザーIDを取得
    $stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
    $stmt->bind_param("s", $_SESSION['user']);
    $stmt->execute();
    $stmt->bind_result($user_id);
    $stmt->fetch();
    $stmt->close();

    // 薬品を登録
    $stmt = $conn->prepare("INSERT INTO medications (user_id, trade_name, quantity) VALUES (?, ?, ?)");
    $stmt->bind_param("isi", $user_id, $trade_name, $quantity);

    if ($stmt->execute()) {
        echo "<div class='alert alert-success'>薬品が登録されました！</div>";
    } else {
        echo "<div class='alert alert-danger'>エラーが発生しました。</div>";
    }
    $stmt->close();
}
?>
<form method="post" class="mt-4">
    <div class="mb-3">
        <label for="trade_name" class="form-label">薬品名</label>
        <input type="text" name="trade_name" id="trade_name" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="quantity" class="form-label">初期在庫数</label>
        <input type="number" name="quantity" id="quantity" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-primary">登録</button>
</form>
<a href="dashboard.php" class="btn btn-secondary mt-3">戻る</a>
<?php include 'footer.php'; ?>