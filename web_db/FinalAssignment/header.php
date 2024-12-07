<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= isset($pageTitle) ? htmlspecialchars($pageTitle) : "残薬管理アプリ" ?></title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- カスタムCSS -->
    <link rel="stylesheet" href="css/style.css">

    <!-- 動的に favicon を指定 -->
    <?php
    // 現在のスクリプトが属するディレクトリを取得
    $baseDir = dirname($_SERVER['SCRIPT_NAME']);

    // デフォルトの favicon パス
    $favicon_path = $baseDir . "/favicon.ico";

    // 他の条件が必要なら追加可能
    ?>
    <link rel="icon" href="<?= htmlspecialchars($favicon_path, ENT_QUOTES, 'UTF-8') ?>" type="image/x-icon">
</head>
<body>
    <!-- ナビゲーションバー -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="dashboard.php">残薬管理アプリ</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="dashboard.php">ダッシュボード</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="add_medication.php">薬品登録</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="manage_medications.php">薬品管理</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="manage_presets.php">プリセット管理</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="view_logs.php">服用履歴</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="account_settings.php">アカウント情報編集</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="logout.php">ログアウト</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-4">