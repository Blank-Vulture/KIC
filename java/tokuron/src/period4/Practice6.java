package period4;

import java.util.Scanner;

public class Practice6 {

    public static void main(String[] args) {
        // 配列の宣言と初期化
        int[] numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

        // スキャナーのセットアップ
        Scanner scanner = new Scanner(System.in);
        int index;

        while (true) {
            // 数字を入力させる
            System.out.print("1から10の数字を入力してください: ");
            index = scanner.nextInt();

            // 入力が1から10の範囲内かチェック
            if (index >= 1 && index <= 10) {
                // 正しい範囲の場合、対応する配列の要素を表示
                System.out.println("対応する値は: " + numbers[index - 1]);
            } else {
                // 範囲外の場合、終了
                System.out.println("入力が範囲外です。プログラムを終了します。");
                break;
            }
        }

        // スキャナーを閉じる
        scanner.close();
    }
}