package period4.Kadai3;

import java.util.Scanner;

public class Mondai2 {

    public static void main(String[] args) {
        // 要素数3のint型配列を準備し、初期値を設定
        int[] numbers = {3, 4, 9};

        // 画面にメッセージを表示
        System.out.println("1桁の数字を入力してください:");

        // キーボードから数字の入力を受け付け
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        // 配列をループで回しながら入力と一致するかを確認
        boolean found = false;
        for (int number : numbers) {
            if (number == input) {
                found = true;
                break;
            }
        }

        // 結果を表示
        if (found) {
            System.out.println("アタリ！");
        } else {
            System.out.println("ハズレ");
        }

        // スキャナーを閉じる
        scanner.close();
    }
}