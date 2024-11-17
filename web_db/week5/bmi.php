<?php
// bmiを計算する関数
function bmi($weight, $height) {
    return $weight / ($height * $height);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $weight = $_POST['weight'];
    $height = $_POST['height'];
    $bmi = bmi($weight, $height);
    echo "BMI: $bmi";
}

?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>BMI計算</title>
</head>
<body>
    <h1>BMI計算</h1>
    <form method="post" action="bmi.php">
        <label>体重(kg): <input type="text" name="weight"></label><br>
        <label>身長(m): <input type="text" name="height"></label><br>
        <input type="submit" value="計算">
    </form>
</body>
</html>