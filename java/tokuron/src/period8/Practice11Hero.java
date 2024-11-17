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
