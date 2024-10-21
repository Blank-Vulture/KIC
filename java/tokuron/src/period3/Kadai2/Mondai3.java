package period3.Kadai2;

import java.util.Random;
import java.util.Scanner;

public class Mondai3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // 2. 0から9までの整数の中からランダムな数を生成し変数ansに代入
        int ans = random.nextInt(10);

        // 3. 5回繰り返すループ
        for (int i = 0; i < 5; i++) {
            // 4. ユーザーに入力を促す
            System.out.print("0～9の数字を入力してください: ");
            int num = scanner.nextInt();

            // 6. 入力された数がansと等しい場合
            if (num == ans) {
                System.out.println("アタリ！");
                break; // 繰り返しを終了
            } else {
                // 7. 等しくない場合
                System.out.println("違います");
            }
        }

        // 8. ゲーム終了メッセージ
        System.out.println("ゲームを終了します");

        scanner.close();
    }

}
