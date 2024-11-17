package period10.Practice15;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // 各怪物のインスタンスを生成
            PoisonMatango poisonMatango = new PoisonMatango();
            GhostBat ghostBat = new GhostBat();
            Goblin goblin = new Goblin();

            while (true) {
                System.out.println("どの怪物で攻撃しますか? 1:毒キノコ 2:お化けコウモリ 3:ゴブリン 9:終了");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1:
                        poisonMatango.fight();
                        break;
                    case 2:
                        ghostBat.fight();
                        break;
                    case 3:
                        goblin.fight();
                        break;
                    case 9:
                        System.out.println("終了します");
                        return;
                    default:
                        System.out.println("正しい数字を入力してください。");
                }
            }
        }
    }
}