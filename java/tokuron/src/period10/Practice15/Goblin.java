package period10.Practice15;

public class Goblin extends Monster {
    public Goblin() {
        super("ゴブリン", 60); // 名前とHPを設定
    }

    @Override
    public void fight() {
        System.out.println(name + "は、殴りかかった。");
    }
}