<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$pageTitle = "ダッシュボード";
include 'header.php';
include 'db_config.php';

// 現在ログイン中のユーザーIDを取得
$stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
$stmt->bind_param("s", $_SESSION['user']);
$stmt->execute();
$stmt->bind_result($user_id);
$stmt->fetch();
$stmt->close();

// プリセット一覧を取得
$stmt = $conn->prepare("
    SELECT p.id AS preset_id, p.name AS preset_name
    FROM presets p
    WHERE p.user_id = ?
");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$presets = $stmt->get_result();
?>

<h1 class="mt-4">ダッシュボード</h1>
<p>ようこそ、<?= htmlspecialchars($_SESSION['user']) ?>さん！</p>

<?php if (isset($_SESSION['feedback_message'])): ?>
<div class="alert alert-success"><?= htmlspecialchars($_SESSION['feedback_message']) ?></div>
<?php unset($_SESSION['feedback_message']); ?>
<?php endif; ?>

<h2 class="mt-4">プリセット一覧</h2>

<div class="row">
    <?php while ($preset = $presets->fetch_assoc()): ?>
    <div class="col-md-4 mb-3">
        <div class="card">
            <div class="card-header">
                <?= htmlspecialchars($preset['preset_name']) ?>
            </div>
            <div class="card-body">
                <h5 class="card-title">薬品一覧</h5>
                <ul class="list-group list-group-flush">
                    <?php
                    // プリセット内の薬品を取得
                    $stmt = $conn->prepare("
                        SELECT m.trade_name, pd.quantity
                        FROM preset_details pd
                        INNER JOIN medications m ON pd.medication_id = m.id
                        WHERE pd.preset_id = ?
                    ");
                    $stmt->bind_param("i", $preset['preset_id']);
                    $stmt->execute();
                    $details = $stmt->get_result();
                    while ($detail = $details->fetch_assoc()):
                    ?>
                    <li class="list-group-item">
                        <?= htmlspecialchars($detail['trade_name']) ?> (<?= $detail['quantity'] ?>錠)
                    </li>
                    <?php endwhile; ?>
                </ul>
            </div>
            <div class="card-footer text-center">
                <a href="edit_preset.php?preset_id=<?= $preset['preset_id'] ?>" class="btn btn-secondary btn-sm">編集</a>
                <form method="post" action="use_preset.php" style="display:inline;">
                    <input type="hidden" name="preset_id" value="<?= $preset['preset_id'] ?>">
                    <button type="submit" class="btn btn-primary btn-sm use-preset-button" data-preset-name="<?= htmlspecialchars($preset['preset_name']) ?>">服用</button>
                </form>
            </div>
        </div>
    </div>
    <?php endwhile; ?>
</div>

<?php include 'footer.php'; ?>