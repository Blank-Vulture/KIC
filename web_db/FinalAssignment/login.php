<?php
$pageTitle = "ログイン";
include 'header.php';

require 'vendor/autoload.php';
include 'db_config.php';

use PHPGangsta_GoogleAuthenticator;

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST['username'];
    $otp = $_POST['otp'];

    // データベースからユーザー情報を取得
    $stmt = $conn->prepare("SELECT otp_secret FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->bind_result($secret);
    $stmt->fetch();

    if ($secret) {
        $gAuth = new PHPGangsta_GoogleAuthenticator();
        if ($gAuth->verifyCode($secret, $otp, 2)) { // 2 = 許容時間の前後30秒
            session_start();
            $_SESSION['user'] = $username;
            header("Location: dashboard.php");
            exit();
        } else {
            echo "<div class='alert alert-danger'>OTPが無効です。</div>";
        }
    } else {
        echo "<div class='alert alert-danger'>ユーザーが存在しません。</div>";
    }
}
?>
<form method="post" class="mt-4">
    <div class="mb-3">
        <label for="username" class="form-label">ユーザー名</label>
        <input type="text" name="username" id="username" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="otp" class="form-label">ワンタイムパスワード</label>
        <input type="text" name="otp" id="otp" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-primary">ログイン</button>
</form>
<a href="index.php" class="btn btn-secondary mt-3">戻る</a>
<?php include 'footer.php'; ?>