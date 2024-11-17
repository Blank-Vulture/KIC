package period11;

public class Paa extends ParentHand {
    @Override
    public String getHandName() {
        return "パー";
    }

    @Override
    public int judge(ParentHand opponent) {
        if (opponent instanceof Paa) return 0; // 引き分け
        if (opponent instanceof Goo) return 1; // 勝ち
        return -1; // 負け
    }
}