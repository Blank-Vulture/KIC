package period2.Kadai1;

import java.util.Random;
import java.util.Scanner;

public class Mondai3 {

	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // 1. 「ようこそ占いの館へ」と表示
        System.out.println("ようこそ占いの館へ");

        // 2. 名前を入力してもらう
        System.out.print("あなたの名前を入力してください: ");
        String name = scanner.nextLine();  // 名前をString型の変数nameに格納

        // 4. 年齢を入力してもらう
        System.out.print("あなたの年齢を入力してください: ");
        String ageString = scanner.nextLine();  // 年齢をString型の変数ageStringに格納

        // 6. 年齢をint型に変換
        int age = Integer.parseInt(ageString);  // int型に変換してageに格納

        // 7. 0から3までの乱数を生成し、運勢番号に代入
        int fortune = random.nextInt(4) + 1;  // 運勢番号(1から4)を生成

        // 9. 「占いの結果が出ました！」と表示
        System.out.println("占いの結果が出ました！");

        // 10. 結果を表示
        System.out.println(age + "歳の" + name + "さん、あなたの運気番号は" + fortune + "です");

        // 運勢の詳細を表示
        System.out.println("(1:大吉 2:中吉 3:吉 4:凶)");

        // スキャナを閉じる
        scanner.close();
	}

}
