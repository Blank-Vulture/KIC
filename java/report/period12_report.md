# Java 課題レポート - 第12回
**学籍番号**: 24024
**名前**: 白石鷹也
**授業日**: 11/15

## 練習18
### ソースコード
```java
package period12;

public class Hero {
    // フィールド（カプセル化: private 修飾子を使用）
    private int hp;
    private String name;

    // hp の setter メソッド（100 を超える値を制限）
    public void setHp(int hp) {
        if (hp > 100) {
            this.hp = 100;
        } else {
            this.hp = hp;
        }
    }

    // hp の getter メソッド
    public int getHp() {
        return hp;
    }

    // name の setter メソッド
    public void setName(String name) {
        this.name = name;
    }

    // name の getter メソッド
    public String getName() {
        return name;
    }

    // ヒーローの情報を表示するメソッド
    public void displayStatus() {
        System.out.println("勇者の名前: " + name);
        System.out.println("勇者のHP: " + hp);
    }
}
```

<div style="page-break-before:always"></div>

```java
package period12;

public class Practice18 {
    public static void main(String[] args) {
        // Hero クラスのインスタンスを生成
        Hero hero = new Hero();

        // setter メソッドを使用して名前と HP を設定
        hero.setName("アーサー");
        hero.setHp(120); // 100 を超える値を指定

        // 勇者の情報を表示
        hero.displayStatus();

        // 変更した値を再度確認
        hero.setHp(80); // 100 以下の値を設定
        hero.displayStatus();
    }
}
```

### 実行結果
![eclipse](/Users/pality/portfolio/KIC/java/img/period12.png)

