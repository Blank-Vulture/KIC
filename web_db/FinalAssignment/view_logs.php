<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$pageTitle = "服用履歴";
include 'header.php';
include 'db_config.php';

// 現在ログイン中のユーザーIDを取得
$stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
$stmt->bind_param("s", $_SESSION['user']);
$stmt->execute();
$stmt->bind_result($user_id);
$stmt->fetch();
$stmt->close();

// 服用履歴を取得
$stmt = $conn->prepare("
    SELECT m.trade_name, l.quantity, l.log_date
    FROM medication_logs l
    INNER JOIN medications m ON l.medication_id = m.id
    WHERE m.user_id = ?
    ORDER BY l.log_date DESC
");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$result = $stmt->get_result();
?>
<h2>服用履歴</h2>
<table class="table table-striped">
    <thead>
        <tr>
            <th>薬品名</th>
            <th>服用数</th>
            <th>記録日</th>
        </tr>
    </thead>
    <tbody>
        <?php while ($row = $result->fetch_assoc()): ?>
        <tr>
            <td><?= htmlspecialchars($row['trade_name']) ?></td>
            <td><?= htmlspecialchars($row['quantity']) ?></td>
            <td><?= htmlspecialchars($row['log_date']) ?></td>
        </tr>
        <?php endwhile; ?>
    </tbody>
</table>
<a href="dashboard.php" class="btn btn-secondary mt-3">戻る</a>
<?php include 'footer.php'; ?>