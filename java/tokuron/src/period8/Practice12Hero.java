package period8;

public class Practice12Hero {
    public int hp;
    protected String name;
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
