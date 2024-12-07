<?php
$host = 'localhost';
$dbname = 'med_management';
$user = 'med_user';
$pass = 'XXXXXXX';

$conn = new mysqli($host, $user, $pass, $dbname);

if ($conn->connect_error) {
    die("データベース接続に失敗しました: " . $conn->connect_error);
}
?>