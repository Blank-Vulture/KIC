package period3.Kadai2;

import java.util.Scanner;

public class Mondai2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. メニューの表示
        System.out.print("メニュー 1: 検索 2: 登録 3: 削除 4: 変更＞");

        // 2. 数字を入力し、変数selectedに代入
        int selected = scanner.nextInt();

        // 3. switch文で処理を分岐
        switch (selected) {
            case 1:
                System.out.println("検索します");
                break;
            case 2:
                System.out.println("登録します");
                break;
            case 3:
                System.out.println("削除します");
                break;
            case 4:
                System.out.println("変更します");
                break;
            default:
                // 4. 1から4のいずれでもない場合は何もしない
                break;
        }

        scanner.close();
    }

}
