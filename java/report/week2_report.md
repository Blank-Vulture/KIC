# Java 課題レポート - 第2回
**学籍番号**: 24024
**名前**: 白石鷹也
**授業日**: 10/18

## 練習4-Practice4
### ソースコード
```java
package week2;

import java.util.Scanner;

public class Practice4 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("あなたの年齢を入力してください");
		int age = scanner.nextInt();
		if (age < 18) {
			System.out.println("未成年です");
		} else {
			System.out.println("成人です");
		}
		scanner.close();
	}

}
```

### 実行結果
```
あなたの年齢を入力してください
18
成人です
```

<div style="page-break-before:always"></div>

## 練習5-Practice5
### ソースコード
```java
package week2;

import java.util.Scanner;
import java.util.Random;

public class Practice5 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int select = 0;
		int omikuji = 0;
		int destiny = 0;
		String result = "";

        while(true) {
        	System.out.println("おみくじを引きますか？　Yes:1を入力 No:2を入力");
        	select = scanner.nextInt();
			if (select != 1 && select != 2) {
				System.out.println("正しい文字を入力してください");
				continue;
			}
        	if(select == 2) {
        		System.out.println("終了します");
        		break;
        	}
        	if (select == 1) {
        		omikuji = new Random().nextInt();
        		destiny = omikuji % 5;
        		switch(destiny) {
				case 0:
					result = "大吉";
				case 1:
					result = "中吉";
				case 2:
					result = "小吉";
				case 3:
					result = "吉";
				case 4:
					result = "凶";
        		}
        		System.out.println("あなたの運命数は"+omikuji+"です。"+"運勢は"+result+"です");
        	}
        }
		
		scanner.close();
	}

}
```

### 実行結果
```
おみくじを引きますか？　Yes:1を入力 No:2を入力
1
あなたの運命数は1997323404です。運勢は凶です
おみくじを引きますか？　Yes:1を入力 No:2を入力
2
終了します
```

<div style="page-break-before:always"></div>

## 問題1-Mondai1
### ソースコード
```java
package week2.Kadai2;

public class Mondai1 {

    public static void main(String[] args) {
        // 1. int型の変数isHungryを定義し、任意で0か1を代入する
        int isHungry = 1;
        //    String型の変数foodを定義し、適当な食べものの名前を代入する
        String food = "おにぎり";

        // 2. 画面に「こんにちは」と表示する
        System.out.println("こんにちは");

        // 3. もし変数isHungryが0であれば「お腹がいっぱいです」、そうでなければ「はらぺこです」と表示する
        if (isHungry == 0) {
            System.out.println("お腹がいっぱいです");
        } else {
            System.out.println("はらぺこです");
        }

        // 4. もしisHungryが空腹を示すならば、変数foodを利用して「○○をいただきます」と表示する
        if (isHungry == 1) {
            System.out.println(food + "をいただきます");
        }

        // 5. 最後に「ごちそうさまでした」と表示する
        System.out.println("ごちそうさまでした");
    }

}
```

### 実行結果
```
こんにちは
はらぺこです
おにぎりをいただきます
ごちそうさまでした
```

<div style="page-break-before:always"></div>

## 問題2-Mondai2
### ソースコード
```java
package week2.Kadai2;

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
```

### 実行結果
```
メニュー 1: 検索 2: 登録 3: 削除 4: 変更＞2
登録します
```

<div style="page-break-before:always"></div>

## 問題3-Mondai3
### ソースコード
```java
package week2.Kadai2;

import java.util.Scanner;
import java.util.Random;

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
```

### 実行結果
```
0～9の数字を入力してください: 1
違います
0～9の数字を入力してください: 2
違います
0～9の数字を入力してください: 3
違います
0～9の数字を入力してください: 4
アタリ！
ゲームを終了します
```


## 備考
eclipseを用いて課題を行いました。
![eclipse](/Users/pality/portfolio/KIC/java/img/period2.png)
