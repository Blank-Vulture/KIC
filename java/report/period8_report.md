# Java 課題レポート - 第8回
**学籍番号**: 24024
**名前**: 白石鷹也
**授業日**: 11/01

## 問題4
### ソースコード
```java
package period8.Kadai5;
import java.util.Random;
public class Claric {
    // フィールド
    public String name;
    public int hp;
    public int maxHp = 50;     // 最大HPの初期値は50
    public int mp;
    public int maxMp = 10;     // 最大MPの初期値は10

    // コンストラクタ
    public Claric(String name) {
        this.name = name;
        this.hp = maxHp;        // 初期HPは最大HP
        this.mp = maxMp;        // 初期MPは最大MP
    }
    // selfAidメソッド
    public void selfAid() {
        if (this.mp >= 5) {
            this.mp -= 5;
            this.hp = this.maxHp;
            System.out.println(this.name + "はセルフエイドを唱えた！ HPが最大まで回復した。");
        } else {
            System.out.println("MPが足りないため、セルフエイドが使えない。");
        }
    }
    // prayメソッド
    public int pray(int seconds) {
        System.out.println(this.name + "は" + seconds + "秒間祈った！");
        Random rand = new Random();
        int recovery = seconds + rand.nextInt(3);  // 0～2ポイントのランダム補正を加える
        int actualRecovery = Math.min(this.maxMp - this.mp, recovery); // 最大MPを超えないように調整
        this.mp += actualRecovery;
        System.out.println("MPが" + actualRecovery + "回復した。");
        return actualRecovery;
    }
}
```

<div style="page-break-before:always"></div>

## 問題5
### ソースコード
```java
package period8.Kadai5;

public class Thief {
    String name;
    int hp;
    int mp;

    // コンストラクタ1: 名前、HP、MPを指定する
    public Thief(String name, int hp, int mp) {
        this.name = name;
        this.hp = hp;
        this.mp = mp;
    }

    // コンストラクタ2: 名前、HPを指定する（MPは5で初期化）
    public Thief(String name, int hp) {
        this(name, hp, 5); // 他のコンストラクタを呼び出し
    }

    // コンストラクタ3: 名前のみ指定する（HPは40、MPは5で初期化）
    public Thief(String name) {
        this(name, 40, 5); // 他のコンストラクタを呼び出し
    }

    // コンストラクタ4: 引数なし（エラーとして初期化できないメッセージ）
    public Thief() {
        System.out.println("名前のないThiefは仮想世界に生み出せない。");
    }
}
```

<div style="page-break-before:always"></div>


## 練習11
### ソースコード
```java
package period8;

import java.util.Scanner;

public class Practice11 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) { // try-with-resources構文でScannerを管理
            // 勇者の名前を入力
            System.out.print("勇者の名前を付けて下さい: ");
            String heroName = scanner.nextLine();
            Practice11Hero hero = new Practice11Hero(heroName);
            System.out.println("勇者は" + heroName + "と名付けられた");

            // 指示を出すループ
            while (true) {
                System.out.println("勇者" + heroName + "は冒険に出かけた。指示をしてください。");
                System.out.println("1:戦う 2:逃げる 3:眠る 9:終了");

                int command = scanner.nextInt();

                switch (command) {
                    case 1:
                        hero.fight();
                        break;
                    case 2:
                        hero.runAway();
                        break;
                    case 3:
                        hero.sleep();
                        break;
                    case 9:
                        hero.endAdventure();
                        break;
                    default:
                        hero.pass();
                        break;
                }
            }
        }
    }
}
```

<div style="page-break-before:always"></div>

### 実行結果
![eclipse](/Users/pality/portfolio/KIC/java/img/period8Practice11.png)

<div style="page-break-before:always"></div>

## 練習11
### ソースコード
```java
package period8;

class Practice11Hero {
	private int hp;
	private String name;
	
	public Practice11Hero(String name) {
        this.hp = 100;
        this.name = name;
    }
	
    // 戦うメソッド
    public void fight() {
        this.hp -= 20;
        System.out.println("勇者" + this.name + "は戦った。 hp:" + this.hp);
        if (this.hp <= 0) {
            System.out.println("勇者" + this.name + "は死亡した");
            System.exit(0);
        }
    }
    
    // 逃げるメソッド
    public void runAway() {
        System.out.println("勇者" + this.name + "は逃げた。");
    }
    
    // 眠るメソッド
    public void sleep() {
        this.hp = 100;
        System.out.println("勇者" + this.name + "は眠って、hpを回復した");
    }
    
    // 終了メソッド
    public void endAdventure() {
        System.out.println("勇者" + this.name + "の冒険は終了した");
        System.exit(0);
    }
    
    // スルーメソッド
    public void pass() {
        System.out.println("勇者" + this.name + "はスルーした");
    }
}
```

<div style="page-break-before:always"></div>

## 練習12
### ソースコード
```java
package period8;
import java.util.Scanner;
public class Practice12 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // 勇者と剣の名前を入力
            System.out.print("勇者の名前を付けて下さい: ");
            String heroName = scanner.nextLine();
            System.out.print("剣の名前を付けて下さい: ");
            String swordName = scanner.nextLine();
            // 剣と勇者のインスタンスを作成
            Practice12Sword sword = new Practice12Sword(swordName);
            Practice12Hero hero = new Practice12Hero(heroName, sword);
            System.out.println("勇者は" + heroName + "と名付けられた");
            System.out.println("剣は" + swordName + "と名付けられた");
            // 指示を出すループ
            while (true) {
                System.out.println("勇者" + heroName + "は冒険に出かけた。指示をしてください。");
                System.out.println("1:戦う 2:逃げる 3:眠る 4:剣で戦う 9:終了");
                int command = scanner.nextInt();
                switch (command) {
                    case 1:
                        hero.fight();
                        break;
                    case 2:
                        hero.runAway();
                        break;
                    case 3:
                        hero.sleep();
                        break;
                    case 4:
                        hero.swordFight();
                        break;
                    case 9:
                        hero.endAdventure();
                        break;
                    default:
                        hero.pass();
                        break;
                }
            }
        }
    }
}
```

<div style="page-break-before:always"></div>

### 実行結果
![eclipse](/Users/pality/portfolio/KIC/java/img/period8Practice12.png)

<div style="page-break-before:always"></div>

## 練習12
### ソースコード
```java
package period8;

public class Practice12Hero {
    private int hp;
    private String name;
    private Practice12Sword sword; // 剣フィールドを追加

    // コンストラクタ
    public Practice12Hero(String name, Practice12Sword sword) {
        this.hp = 100;
        this.name = name;
        this.sword = sword;
    }

    // 戦うメソッド
    public void fight() {
        this.hp -= 20;
        System.out.println("勇者" + this.name + "は戦った。 hp:" + this.hp);
        if (this.hp <= 0) {
            System.out.println("勇者" + this.name + "は死亡した");
            System.exit(0);
        }
    }

    // 剣で戦うメソッド
    public void swordFight() {
        System.out.println("勇者" + this.name + "は" + sword.getName() + "を使って戦った。 相手に" + sword.getDamage() + "のダメージを与えた");
    }

    // 逃げるメソッド
    public void runAway() {
        System.out.println("勇者" + this.name + "は逃げた。");
    }

    // 眠るメソッド
    public void sleep() {
        this.hp = 100;
        System.out.println("勇者" + this.name + "は眠って、hpを回復した");
    }

    // 終了メソッド
    public void endAdventure() {
        System.out.println("勇者" + this.name + "の冒険は終了した");
        System.exit(0);
    }

    // スルーメソッド
    public void pass() {
        System.out.println("勇者" + this.name + "はスルーした");
    }
}
```


<div style="page-break-before:always"></div>

## 練習12
### ソースコード
```java
package period8;

public class Practice12Sword {
    private String name;        // 剣の名前
    private int damage;         // 与えるダメージ
    // コンストラクタ
    public Practice12Sword(String name) {
        this.name = name;
        this.damage = 20;       // ダメージは固定で20
    }
    // 名前を取得するメソッド
    public String getName() {
        return name;
    }
    // ダメージを取得するメソッド
    public int getDamage() {
        return damage;
    }
}
```


