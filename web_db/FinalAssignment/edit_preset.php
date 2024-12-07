<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$pageTitle = "プリセット編集";
include 'header.php';
include 'db_config.php';

// 現在ログイン中のユーザーIDを取得
$stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
$stmt->bind_param("s", $_SESSION['user']);
$stmt->execute();
$stmt->bind_result($user_id);
$stmt->fetch();
$stmt->close();

// プリセットIDと名前の取得
$preset_id = $_GET['preset_id'] ?? null;
if (!$preset_id) {
    echo "<div class='alert alert-danger'>プリセットIDが指定されていません。</div>";
    exit();
}

$stmt = $conn->prepare("SELECT name FROM presets WHERE id = ?");
$stmt->bind_param("i", $preset_id);
$stmt->execute();
$stmt->bind_result($preset_name);
$stmt->fetch();
$stmt->close();

// 薬品追加処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['add_medication'])) {
    $medication_id = $_POST['medication_id'];
    $quantity = $_POST['quantity'];

    $stmt = $conn->prepare("INSERT INTO preset_details (preset_id, medication_id, quantity) VALUES (?, ?, ?)");
    $stmt->bind_param("iii", $preset_id, $medication_id, $quantity);

    if ($stmt->execute()) {
        echo "<div class='alert alert-success'>薬品が追加されました！</div>";
    } else {
        echo "<div class='alert alert-danger'>薬品の追加に失敗しました。</div>";
    }
    $stmt->close();
}

// 薬品削除処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['delete_detail'])) {
    $detail_id = $_POST['detail_id'];

    $stmt = $conn->prepare("DELETE FROM preset_details WHERE id = ?");
    $stmt->bind_param("i", $detail_id);

    if ($stmt->execute()) {
        echo "<div class='alert alert-success'>薬品が削除されました！</div>";
    } else {
        echo "<div class='alert alert-danger'>薬品の削除に失敗しました。</div>";
    }
    $stmt->close();
}

// 薬品編集処理
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['edit_detail'])) {
    $detail_id = $_POST['detail_id'];
    $quantity = $_POST['quantity'];

    $stmt = $conn->prepare("UPDATE preset_details SET quantity = ? WHERE id = ?");
    $stmt->bind_param("ii", $quantity, $detail_id);

    if ($stmt->execute()) {
        echo "<div class='alert alert-success'>服用数が更新されました！</div>";
    } else {
        echo "<div class='alert alert-danger'>服用数の更新に失敗しました。</div>";
    }
    $stmt->close();
}

// 薬品リストとプリセット内の薬品を再取得
$stmt = $conn->prepare("SELECT id, trade_name FROM medications WHERE user_id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$medications = $stmt->get_result();

$stmt = $conn->prepare("
    SELECT pd.id AS detail_id, m.trade_name, pd.quantity
    FROM preset_details pd
    INNER JOIN medications m ON pd.medication_id = m.id
    WHERE pd.preset_id = ?
");
$stmt->bind_param("i", $preset_id);
$stmt->execute();
$details = $stmt->get_result();
?>
<h2>プリセット編集: <?= htmlspecialchars($preset_name) ?></h2>

<!-- 薬品追加フォーム -->
<form method="post" class="mt-4">
    <div class="mb-3">
        <label for="medication_id" class="form-label">薬品</label>
        <select name="medication_id" id="medication_id" class="form-select" required>
            <?php while ($med = $medications->fetch_assoc()): ?>
                <option value="<?= $med['id'] ?>"><?= htmlspecialchars($med['trade_name']) ?></option>
            <?php endwhile; ?>
        </select>
    </div>
    <div class="mb-3">
        <label for="quantity" class="form-label">服用数</label>
        <input type="number" name="quantity" id="quantity" class="form-control" required>
    </div>
    <button type="submit" name="add_medication" class="btn btn-primary">薬品追加</button>
</form>

<!-- 現在の薬品一覧 -->
<h3 class="mt-4">現在の薬品一覧</h3>
<table class="table table-striped">
    <thead>
        <tr>
            <th>薬品名</th>
            <th>服用数</th>
            <th>操作</th>
        </tr>
    </thead>
    <tbody>
        <?php while ($detail = $details->fetch_assoc()): ?>
        <tr>
            <td><?= htmlspecialchars($detail['trade_name']) ?></td>
            <td>
                <!-- 服用数編集フォーム -->
                <form method="post" style="display:inline;">
                    <input type="hidden" name="detail_id" value="<?= $detail['detail_id'] ?>">
                    <input type="number" name="quantity" value="<?= $detail['quantity'] ?>" class="form-control d-inline-block" style="width: 100px;">
                    <button type="submit" name="edit_detail" class="btn btn-primary btn-sm">更新</button>
                </form>
            </td>
            <td>
                <!-- 削除フォーム -->
                <form method="post" style="display:inline;">
                    <input type="hidden" name="detail_id" value="<?= $detail['detail_id'] ?>">
                    <button type="submit" name="delete_detail" class="btn btn-danger btn-sm">削除</button>
                </form>
            </td>
        </tr>
        <?php endwhile; ?>
    </tbody>
</table>

<a href="manage_presets.php" class="btn btn-secondary mt-3">戻る</a>
<?php include 'footer.php'; ?>