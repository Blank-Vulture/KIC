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
