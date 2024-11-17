package period5;
import java.util.Scanner;
public class Practice8 {

    public static void main(String[] args) {
        boolean[] loop = {true};
        Scanner scanner = new Scanner(System.in);

        while (loop[0]) {
            System.out.println("どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4");
            int input = scanner.nextInt();

            // 入力に基づいて鳴き声を取得
            String result = getAnimalSound(input, loop);
            System.out.println(result);
        }

        scanner.close();
    }

    // 動物の鳴き声を取得するメソッド
    public static String getAnimalSound(int input, boolean[] loop) {
        String result;
        switch (input) {
            case 1:
                result = "犬の鳴き声はワンワンです";
                break;
            case 2:
                result = "猫の鳴き声はニャーニャーです";
                break;
            case 3:
                result = "虎の鳴き声はガオーです";
                break;
            case 4:
                // 終了処理を呼び出し（オーバーロード使用）
                result = endProgram();
                break;
            default:
                result = "正しい数字を入力してください";
        }
        return result;
    }

    // 終了処理のオーバーロード（引数なし）
    public static String endProgram() {
        return endProgram("終了します");
    }

    // 終了処理のオーバーロード（引数あり）
    public static String endProgram(String message) {
        // 実際の終了処理
        System.out.println(message);
        System.exit(0); // プログラムを終了する
        return message;
    }

}
