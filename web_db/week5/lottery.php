<?php
function predictLottoNumbers() {
    $predictedNumbers = [];

    // ランダムに10個の番号を生成して配列に追加
    for ($i = 0; $i < 10; $i++) {
        // 宝くじの番号を1から100000の範囲でランダムに生成
        $number = rand(1, 100000);

        // 重複を避けるために、既に存在する番号は生成し直す
        while (in_array($number, $predictedNumbers)) {
            $number = rand(1, 49);
        }

        $predictedNumbers[] = $number;
    }

    return $predictedNumbers;
}

// 関数を呼び出して結果を表示
$predictedNumbers = predictLottoNumbers();
echo "予測された宝くじの当選番号: ";
echo implode(", ", $predictedNumbers);
?>