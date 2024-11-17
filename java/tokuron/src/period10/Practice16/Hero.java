package period10.Practice16;

public class Hero extends Human {
    public Hero(String name) {
        super(name);
    }

    @Override
    public void run() {
        System.out.println("勇者" + name + "は走って逃げた");
    }

    @Override
    public void talk() {
        System.out.println("勇者" + name + "は元気よく話した");
    }

    @Override
    public void attack() {
        System.out.println("勇者" + name + "は剣を使って戦った");
    }
}
