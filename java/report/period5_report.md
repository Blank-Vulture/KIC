# Java 課題レポート - 第5回
**学籍番号**: 24024
**名前**: 白石鷹也
**授業日**: 10/25

## 練習8
### ソースコード
```java
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

## 課題004
## 問題1
### ソースコード
```java
package period5.Kadai4;

public class Mondai1 {

	public static void main(String[] args) {
		String title = "お知らせ";
		String address = "info@example.com";
		String text = "新しい情報です";
		
		email(title, address, text);

	}
	
	//emailメソッドを定義
	//戻り値：なし
	//引数：String title, String address, String text
	//処理：以下の形式で表示を行う
	// メールの宛先アドレス(address)に、以下のメールを送信しました
	// 件名：title
	// 本文：text
	public static void email(String title, String address, String text) {
		System.out.println(address + "に、以下のメールを送信しました");
		System.out.println("件名：" + title);
		System.out.println("本文：" + text);
	}

}
```

### 実行結果
```
info@example.comに、以下のメールを送信しました
件名：お知らせ
本文：新しい情報です
```

<div style="page-break-before:always"></div>

## 問題2
### ソースコード
```java
package period5.Kadai4;
//import period5.Kadai4.Mondai1;
public class Mondai2 {

	public static void main(String[] args) {
		String address = "info@example.com";
		String text = "javaの勉強をしています";
		
		email(address, text);
	}
	
	//emailメソッドをオーバーロード
	//titleは無題
	public static void email(String address, String text) {
	    // importしているperiod5.Kadai4.Mondai1クラスのemailメソッドを呼び出す
		Mondai1.email("無題", address, text);
	}

}
```

### 実行結果
```
info@example.comに、以下のメールを送信しました
件名：無題
本文：javaの勉強をしています
```

<div style="page-break-before:always"></div>

## 備考
eclipseを用いて課題を行いました。
![eclipse](/Users/pality/portfolio/KIC/java/img/period5.png)
