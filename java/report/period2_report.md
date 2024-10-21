# Java 課題レポート - 第2回
**学籍番号**: 24024
**名前**: 白石鷹也
**授業日**: 10/18

## 練習1-Practice1
### ソースコード
```java

package period2;

public class Practice1 {
	public static void main(String[] args) {
		System.out.println("Takaya Shiraishi");
	}
}

```

### 実行結果
```
（実行結果を貼り付けてください）
```

<div style="page-break-before:always"></div>

## 練習2-Practice2
### ソースコード
```java

package period2;

public class Practice2 {

	public static void main(String[] args) {
		// $name, $favoriteNum
		String name = "白石 鷹也";
		int favoriteNum = 0;
		System.out.println("私の名前は" + name + "です。"+ "好きな数字は" + favoriteNum + "です。");
		// 正常終了のためのステータスコードなので、好きです
	}

}

```

### 実行結果
```
（実行結果を貼り付けてください）
```

<div style="page-break-before:always"></div>

## 練習3-Practice3
### ソースコード
```java

package period2;

public class Practice3 {

	public static void main(String[] args) {
		// キャストによるデータ破損の確認
		double rawPi = 0.0;
		
		// ライプニッツの公式で円周率を求める
		for (int i = 1; i < 100000; i++) {
			if (i % 2 == 0) {
				rawPi -= 1.0 / (2 * i - 1);
			} else {
				rawPi += 1.0 / (2 * i - 1);
			}
		}
		rawPi *= 4;
		
		int droppedPi = (int) rawPi;
		System.out.println("キャスト前(double): "+rawPi);
		System.out.println("キャスト後(int): "+droppedPi);
	}

}

```

### 実行結果
```
（実行結果を貼り付けてください）
```

<div style="page-break-before:always"></div>

## 問題1-Mondai1
### ソースコード
```java

package period2.Kadai1;

public class Mondai1 {

	public static void main(String[] args) {
		// 長方形の面積
		int a = 3;
		int b = 5;
		int c = a * b;
	    System.out.println("縦幅"+a+"横幅"+b+"の長方形の面積は、"+c);

	}

}

```

### 実行結果
```
（実行結果を貼り付けてください）
```

<div style="page-break-before:always"></div>

## 問題2-Mondai2
### ソースコード
```java

package period2.Kadai1;
public class Mondai2 {
	public static void main(String[] args) {
		int x = 5;
		int y = 10;
		String ans = "x+y=" + (x + y);
		System.out.println(ans);
	}
}
```

### 実行結果
```
（実行結果を貼り付けてください）
```

<div style="page-break-before:always"></div>

## 問題3-Mondai3
### ソースコード
```java

package period2.Kadai1;

import java.util.Scanner;
import java.util.Random;

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

```

### 実行結果
```
（実行結果を貼り付けてください）
```

<div style="page-break-before:always"></div>

## 備考
eclipseを用いて課題を行いました。
![eclipse](/Users/pality/portfolio/KIC/java/img/period2.png)
