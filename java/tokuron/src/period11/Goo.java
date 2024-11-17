package period11;

public class Goo extends ParentHand {
    @Override
    public String getHandName() {
        return "グー";
    }

    @Override
    public int judge(ParentHand opponent) {
        if (opponent instanceof Goo) return 0; // 引き分け
        if (opponent instanceof Choki) return 1; // 勝ち
        return -1; // 負け
    }
}