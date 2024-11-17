# Java 課題レポート - 第11回
**学籍番号**: 24024
**名前**: 白石鷹也
**授業日**: 11/15

## 練習17
### ソースコード
```java
package period11;

public class Choki extends ParentHand {
    @Override
    public String getHandName() {
        return "チョキ";
    }

    @Override
    public int judge(ParentHand opponent) {
        if (opponent instanceof Choki) return 0; // 引き分け
        if (opponent instanceof Paa) return 1; // 勝ち
        return -1; // 負け
    }
}
```

```java
package period11;

public class Goo extends ParentHand {
    @Override
    public String getHandName() {
        return "グー";
    }

    @Override
    public int judge(ParentHand opponent) {
        if (opponent instanceof Goo) return 0; // 引き分け
        if (opponent instanceof Choki) return 1; // 勝ち
        return -1; // 負け
    }
}
```

<div style="page-break-before:always"></div>

```java
package period11;

public class Paa extends ParentHand {
    @Override
    public String getHandName() {
        return "パー";
    }

    @Override
    public int judge(ParentHand opponent) {
        if (opponent instanceof Paa) return 0; // 引き分け
        if (opponent instanceof Goo) return 1; // 勝ち
        return -1; // 負け
    }
}
```

```java
package period11;

public abstract class ParentHand {
    public abstract String getHandName();

    // 勝敗を判定するメソッド
    public abstract int judge(ParentHand opponent);
}
```

<div style="page-break-before:always"></div>

```java
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
```

<div style="page-break-before:always"></div>

### 実行結果
![eclipse](/Users/pality/portfolio/KIC/java/img/period11-1.png)

<div style="page-break-before:always"></div>

![eclipse](/Users/pality/portfolio/KIC/java/img/period11-2.png)