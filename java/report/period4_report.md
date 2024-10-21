# Java 課題レポート - 第4回
**学籍番号**: 24024
**名前**: 白石鷹也
**授業日**: 10/18

## 練習6-Practice6
### ソースコード
```java

package period4;

import java.util.Scanner;

public class Practice6 {

    public static void main(String[] args) {
        // 配列の宣言と初期化
        int[] numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

        // スキャナーのセットアップ
        Scanner scanner = new Scanner(System.in);
        int index;

        while (true) {
            // 数字を入力させる
            System.out.print("1から10の数字を入力してください: ");
            index = scanner.nextInt();

            // 入力が1から10の範囲内かチェック
            if (index >= 1 && index <= 10) {
                // 正しい範囲の場合、対応する配列の要素を表示
                System.out.println("対応する値は: " + numbers[index - 1]);
            } else {
                // 範囲外の場合、終了
                System.out.println("入力が範囲外です。プログラムを終了します。");
                break;
            }
        }

        // スキャナーを閉じる
        scanner.close();
    }
}
```

<div style="page-break-before:always"></div>

### 実行結果
```
1から10の数字を入力してください: 8
対応する値は: 80
1から10の数字を入力してください: 1
対応する値は: 10
1から10の数字を入力してください: 0
入力が範囲外です。プログラムを終了します。
```

## 練習7-Practice7
### ソースコード
```java

package period4;

public class Practice7 {

    public static void main(String[] args) {
        // 2次元配列の宣言と初期化
        int[][] numbers = new int[3][3];
        int value = 1;

        // 配列を1から9で初期化
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                numbers[i][j] = value;
                value++;
            }
        }

        // 配列の内容を表示
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(numbers[i][j]);
                if (j < 2) {
                    System.out.print(", "); // カンマ区切り
                }
            }
            System.out.println(); // 改行
        }
    }
}
```

<div style="page-break-before:always"></div>

### 実行結果
```
1, 2, 3
4, 5, 6
7, 8, 9
```

## 問題1-Mondai1
### ソースコード
```java

package period4.Kadai3;

public class Mondai1 {

    public static void main(String[] args) {
        // 3つの口座残高を格納するint型配列を宣言
        int[] moneyList = {121902, 8302, 55100};

        // for文で配列の要素を1つずつ取り出して表示
        System.out.println("for文での表示:");
        for (int i = 0; i < moneyList.length; i++) {
            System.out.println(moneyList[i]);
        }

        // 拡張for文で配列の要素を1つずつ取り出して表示
        System.out.println("拡張for文での表示:");
        for (int money : moneyList) {
            System.out.println(money);
        }
    }
}
```

### 実行結果
```
for文での表示:
121902
8302
55100
拡張for文での表示:
121902
8302
55100
```

<div style="page-break-before:always"></div>

## 問題2-Mondai2
### ソースコード
```java

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
```

<div style="page-break-before:always"></div>

### 実行結果
```
1桁の数字を入力してください:
2
ハズレ
```

```
1桁の数字を入力してください:
9
アタリ！
```

## 備考
eclipseを用いて課題を行いました。
![eclipse](/Users/pality/portfolio/KIC/java/img/period4.png)
