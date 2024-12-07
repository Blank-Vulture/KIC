<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

include 'db_config.php';

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['preset_id'])) {
    $preset_id = $_POST['preset_id'];

    // 現在ログイン中のユーザーIDを取得
    $stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
    $stmt->bind_param("s", $_SESSION['user']);
    $stmt->execute();
    $stmt->bind_result($user_id);
    $stmt->fetch();
    $stmt->close();

    // プリセット名を取得
    $stmt = $conn->prepare("SELECT name FROM presets WHERE id = ?");
    $stmt->bind_param("i", $preset_id);
    $stmt->execute();
    $stmt->bind_result($preset_name);
    $stmt->fetch();
    $stmt->close();

    // プリセット内の薬品を取得
    $stmt = $conn->prepare("
        SELECT pd.medication_id, pd.quantity
        FROM preset_details pd
        INNER JOIN medications m ON pd.medication_id = m.id
        WHERE pd.preset_id = ? AND m.user_id = ?
    ");
    $stmt->bind_param("ii", $preset_id, $user_id);
    $stmt->execute();
    $details = $stmt->get_result();

    // 在庫を減少 & 服薬記録を追加
    while ($detail = $details->fetch_assoc()) {
        // 在庫数を減少
        $stmt = $conn->prepare("UPDATE medications SET quantity = quantity - ? WHERE id = ?");
        $stmt->bind_param("ii", $detail['quantity'], $detail['medication_id']);
        $stmt->execute();

        // 服薬記録を追加
        $stmt = $conn->prepare("INSERT INTO medication_logs (medication_id, quantity) VALUES (?, ?)");
        $stmt->bind_param("ii", $detail['medication_id'], $detail['quantity']);
        $stmt->execute();
    }

    // フィードバックをセッションに保存
    $_SESSION['feedback_message'] = "プリセット「" . htmlspecialchars($preset_name) . "」の服用が完了しました！";

    header("Location: dashboard.php");
    exit();
}
?>