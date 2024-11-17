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