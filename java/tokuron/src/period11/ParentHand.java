package period11;

public abstract class ParentHand {
    public abstract String getHandName();

    // 勝敗を判定するメソッド
    public abstract int judge(ParentHand opponent);
}