package period8.Kadai5;
import java.util.Random;
public class Claric {
    // フィールド
    public String name;
    public int hp;
    final int maxHp = 50;     // 最大HPの初期値は50
    public int mp;
    final int maxMp = 10;     // 最大MPの初期値は10

    // コンストラクタ
    public Claric(String name) {
        this.name = name;
        this.hp = maxHp;        // 初期HPは最大HP
        this.mp = maxMp;        // 初期MPは最大MP
    }

    // selfAidメソッド
    public void selfAid() {
        if (this.mp >= 5) {
            this.mp -= 5;
            this.hp = this.maxHp;
            System.out.println(this.name + "はセルフエイドを唱えた！ HPが最大まで回復した。");
        } else {
            System.out.println("MPが足りないため、セルフエイドが使えない。");
        }
    }

    // prayメソッド
    public int pray(int seconds) {
        System.out.println(this.name + "は" + seconds + "秒間祈った！");
        Random rand = new Random();
        int recovery = seconds + rand.nextInt(3);  // 0～2ポイントのランダム補正を加える
        int actualRecovery = Math.min(this.maxMp - this.mp, recovery); // 最大MPを超えないように調整
        this.mp += actualRecovery;
        System.out.println("MPが" + actualRecovery + "回復した。");
        return actualRecovery;
    }
}
