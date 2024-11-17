package period10.Practice15;

public class GhostBat extends Monster {
    public GhostBat() {
        super("お化けコウモリ", 40); // 名前とHPを設定
    }

    @Override
    public void fight() {
        System.out.println(name + "は、空から攻撃した。");
    }
}