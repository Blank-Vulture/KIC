package period11;

import java.util.Random;
import java.util.Scanner;

public class Practice17 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int playerPoints = 0;

        while (true) {
            System.out.println("ジャンケンをしましょう！ 1:チョキ 2:パー 3:グー 9:終了");
            int playerChoice = scanner.nextInt();

            // 終了処理
            if (playerChoice == 9) {
                System.out.println("終了します。");
                break;
            }

            // 入力チェック
            if (playerChoice < 1 || playerChoice > 3) {
                System.out.println("正しい数字を入れて下さい。");
                continue;
            }

            // プレイヤーの手を生成
            ParentHand playerHand = getHand(playerChoice);

            // コンピュータの手を生成
            int computerChoice = random.nextInt(3) + 1;
            ParentHand computerHand = getHand(computerChoice);

            // 勝敗判定
            int result = playerHand.judge(computerHand);

            // 勝敗結果のメッセージ
            String resultMessage;
            if (result == 1) {
                resultMessage = "勝ち";
                playerPoints++;
            } else if (result == -1) {
                resultMessage = "負け";
                playerPoints--;
            } else {
                resultMessage = "あいこ";
            }

            // 結果を表示
            System.out.println("あなたの出した手: " + playerHand.getHandName());
            System.out.println("コンピュータの出した手: " + computerHand.getHandName());
            System.out.println("結果: " + resultMessage);
            System.out.println("現在のポイント: " + playerPoints);

            // 勝敗が決定した場合
            if (playerPoints == 3) {
                System.out.println("3ポイントになったのであなたの勝ちです。");
                break;
            } else if (playerPoints == -3) {
                System.out.println("-3ポイントになったのであなたの負けです。");
                break;
            }
        }

        scanner.close();
    }

    // 手を生成するメソッド
    private static ParentHand getHand(int choice) {
        switch (choice) {
            case 1:
                return new Choki();
            case 2:
                return new Paa();
            case 3:
                return new Goo();
            default:
                throw new IllegalArgumentException("Invalid choice: " + choice);
        }
    }
}