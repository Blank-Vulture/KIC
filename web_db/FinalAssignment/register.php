<?php
$pageTitle = "新規登録";
include 'header.php';

require 'vendor/autoload.php';
include 'db_config.php';

use PHPGangsta_GoogleAuthenticator;

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST['username'];

    // Google Authenticatorのシークレット生成
    $gAuth = new PHPGangsta_GoogleAuthenticator();
    $secret = $gAuth->createSecret();

    // データベースにユーザーを保存
    $stmt = $conn->prepare("INSERT INTO users (username, otp_secret) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $secret);

    if ($stmt->execute()) {
        $qrCodeUrl = $gAuth->getQRCodeGoogleUrl($username, $secret, "MedManagement");
        echo "<div class='alert alert-success'>登録成功！以下のQRコードをスキャンしてください：</div>";
        echo "<img src='$qrCodeUrl' class='img-fluid mb-3'>";
        echo "<p>手動でこのシークレットを入力してください：<strong>$secret</strong></p>";
    } else {
        echo "<div class='alert alert-danger'>エラー: ユーザー名が既に使用されています。</div>";
    }
}
?>
<form method="post" class="mt-4">
    <div class="mb-3">
        <label for="username" class="form-label">ユーザー名</label>
        <input type="text" name="username" id="username" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-primary">登録</button>
</form>
<a href="index.php" class="btn btn-secondary mt-3">戻る</a>
<?php include 'footer.php'; ?>