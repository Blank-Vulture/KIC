package period9;

import period8.Practice12Hero;
import period8.Practice12Sword;

public class Practice14SuperHero extends Practice12Hero {
    private boolean isFlying = false; // 飛行状態を管理するフラグ

    // コンストラクタ：名前と剣を受け取り、親クラスのコンストラクタを呼び出す
    public Practice14SuperHero(String name, Practice12Sword sword) {
        super(name, sword);
    }

    // 通常の「戦う」メソッド（親クラスのメソッドを呼ぶ）
    public void normalFight() {
        super.fight();
    }

    // スーパー勇者として戦うメソッド（オーバーライド）
    @Override
    public void fight() {
        System.out.println("勇者" + this.getName() + "は戦った。 hpは、減らなかった。");
    }

    // 飛ぶメソッド
    public void fly() {
        if (!isFlying) {
            System.out.println("勇者" + this.getName() + "は空を飛んだ。");
            isFlying = true;
        } else {
            System.out.println("勇者" + this.getName() + "は既に空を飛んでいる。");
        }
    }

    // 着陸するメソッド
    public void land() {
        if (isFlying) {
            System.out.println("勇者" + this.getName() + "は着陸した。");
            isFlying = false;
        } else {
            System.out.println("勇者" + this.getName() + "は空を飛んでいないので着陸できない。");
        }
    }

    // 名前を取得するメソッド
    public String getName() {
        return this.name;
    }
}