package period10.Practice16;


public class Werewolf extends Human implements Monster {
    public Werewolf(String name) {
        super(name);
    }

    @Override
    public void run() {
        System.out.println("狼男" + name + "は獣のように走って逃げた");
    }

    @Override
    public void talk() {
        System.out.println("狼男" + name + "は低い声で話した");
    }

    @Override
    public void attack() {
        System.out.println("狼男" + name + "は牙と爪で戦った");
    }

    @Override
    public void howl() {
        System.out.println("狼男" + name + "は吠えた");
    }
}