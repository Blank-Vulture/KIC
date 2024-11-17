package period10.Practice16;

public class Wizard extends Human {
    public Wizard(String name) {
        super(name);
    }

    @Override
    public void run() {
        System.out.println("魔法使い" + name + "は魔法を使って逃げた");
    }

    @Override
    public void talk() {
        System.out.println("魔法使い" + name + "は魔法の呪文で話した");
    }

    @Override
    public void attack() {
        System.out.println("魔法使い" + name + "は魔法を使って戦った");
    }
}
