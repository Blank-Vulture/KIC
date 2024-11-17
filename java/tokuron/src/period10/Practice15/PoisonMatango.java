package period10.Practice15;

public class PoisonMatango extends Monster {
    public PoisonMatango() {
        super("毒キノコ", 50); // 名前とHPを設定
    }

    @Override
    public void fight() {
        System.out.println(name + "は、毒を吐いた。");
    }
}