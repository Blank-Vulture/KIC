package period10.Practice16;


public abstract class Human implements Character {
    protected String name;
    protected int hp;

    public Human(String name) {
        this.name = name;
        this.hp = 100;
    }

    @Override
    public void walk() {
        System.out.println(name + "は歩いています。");
    }

    @Override
    public void sleep() {
        hp = 100;
        System.out.println(name + "は休んで、体力が" + hp + "に回復しました。");
    }

    @Override
    public abstract void run();

    @Override
    public abstract void talk();
}
