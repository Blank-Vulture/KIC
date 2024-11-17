package period9.Kadai6;
public class PoisonMatango extends Matango {
    int poisonCount = 5; // 毒攻撃の残り回数

    public PoisonMatango(char suffix) {
        super(suffix);
    }

    @Override
    public void attack(Hero h) {
        // 通常の攻撃
        super.attack(h);

        // 毒攻撃が可能な場合
        if (poisonCount > 0) {
            System.out.println("さらに毒の胞子をばらまいた！");
            int poisonDamage = h.hp / 5; // 勇者のHPの1/5のダメージ
            h.hp -= poisonDamage;
            System.out.println("ポイントのダメージ！ " + poisonDamage + " のダメージを受けた");
            poisonCount--; // 毒攻撃の残り回数を減らす
        }
    }
}