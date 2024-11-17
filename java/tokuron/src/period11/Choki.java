package period11;

public class Choki extends ParentHand {
    @Override
    public String getHandName() {
        return "チョキ";
    }

    @Override
    public int judge(ParentHand opponent) {
        if (opponent instanceof Choki) return 0; // 引き分け
        if (opponent instanceof Paa) return 1; // 勝ち
        return -1; // 負け
    }
}