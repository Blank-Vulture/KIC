package period8.Kadai5;

public class Thief {
    String name;
    int hp;
    int mp;

    // コンストラクタ1: 名前、HP、MPを指定する
    public Thief(String name, int hp, int mp) {
        this.name = name;
        this.hp = hp;
        this.mp = mp;
    }

    // コンストラクタ2: 名前、HPを指定する（MPは5で初期化）
    public Thief(String name, int hp) {
        this(name, hp, 5); // 他のコンストラクタを呼び出し
    }

    // コンストラクタ3: 名前のみ指定する（HPは40、MPは5で初期化）
    public Thief(String name) {
        this(name, 40, 5); // 他のコンストラクタを呼び出し
    }

    // コンストラクタ4: 引数なし（エラーとして初期化できないメッセージ）
    public Thief() {
        System.out.println("名前のないThiefは仮想世界に生み出せない。");
    }
}
