package period10.Practice15;

public abstract class Monster {
    protected int hp;
    protected String name;

    public Monster(String name, int hp) {
        this.name = name;
        this.hp = hp;
    }

    // 抽象メソッド「戦う」
    public abstract void fight();
}