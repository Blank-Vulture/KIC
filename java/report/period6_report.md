# Java 課題レポート - 第6回
**学籍番号**: 24024
**名前**: 白石鷹也
**授業日**: 10/25

## 練習9
### ソースコード
```java
package period6;
import java.util.Scanner;
public class Practice9 {

	public static void main(String[] args) {
        boolean[] loop = {true};
        Scanner scanner = new Scanner(System.in);
        
        while (loop[0]) {
            System.out.println("どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4");
            int input = scanner.nextInt();
            
            // Voiceクラスのメソッドを呼び出して鳴き声を取得
            String result = Practiced9Voice.getAnimalSound(input, loop);
            System.out.println(result);
        }
        
        scanner.close();		

	}

}
```

### 実行結果
```
どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4
1
犬の鳴き声はワンワンです
どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4
2
猫の鳴き声はニャーニャーです
どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4
3
虎の鳴き声はガオーです
どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4
4
終了します
```

<div style="page-break-before:always"></div>

### クラスのソースコード
```java
package period6;

public class Practiced9Voice {
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
```

<div style="page-break-before:always"></div>

## 練習10
### ソースコード
```java
package period6.practice10.main;
import java.util.Scanner;
import period6.practice10.voice.Voice;
public class Main {

    public static void main(String[] args) {
        boolean[] loop = {true};
        Scanner scanner = new Scanner(System.in);
        
        while (loop[0]) {
            System.out.println("どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4");
            int input = scanner.nextInt();
            
            // Voiceクラスのメソッドを呼び出して鳴き声を取得
            String result = Voice.getAnimalSound(input, loop);
            System.out.println(result);
        }
        
        scanner.close();
    }

}
```

### 実行結果
```
どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4
3
虎の鳴き声はガオーです
どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4
2
猫の鳴き声はニャーニャーです
どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4
5
正しい数字を入力してください
どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4
4
終了します
```

<div style="page-break-before:always"></div>

### ソースコード
```java
package period6.practice10.voice;
public class Voice {
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
```

<div style="page-break-before:always"></div>

## 備考
eclipseを用いて課題を行いました。
![eclipse](/Users/pality/portfolio/KIC/java/img/period6.png)
