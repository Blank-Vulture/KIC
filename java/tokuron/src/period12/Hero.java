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