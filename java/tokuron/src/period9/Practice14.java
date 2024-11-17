package period9;

import java.util.Scanner;

import period8.Practice12Sword;

public class Practice14 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // プレイヤーに名前を入力してもらう
            System.out.print("勇者の名前を付けて下さい: ");
            String heroName = scanner.nextLine();
            System.out.print("剣の名前をつけてください: ");
            String swordName = scanner.nextLine();

            // スーパー勇者を作成し、剣を装備させる
            Practice12Sword sword = new Practice12Sword(swordName);
            Practice14SuperHero hero = new Practice14SuperHero(heroName, sword);
            System.out.println("勇者は" + heroName + "と名付けられた");
            System.out.println("剣は" + swordName + "と名付けられた");

            while (true) {
                System.out.println("勇者" + hero.getName() + "は冒険に出かけた。 指示をしてください。");
                System.out.println("1:戦う 2:逃げる 3:眠る 4:剣で戦う 5:飛ぶ 6:着陸する 7:スーパー勇者として戦う 9:終了");
                int command = scanner.nextInt();

                switch (command) {
                    case 1:
                        hero.normalFight(); // 親クラスの戦うメソッドを呼ぶ
                        break;
                    case 2:
                        hero.runAway();
                        break;
                    case 3:
                        hero.sleep();
                        break;
                    case 4:
                        hero.swordFight();
                        break;
                    case 5:
                        hero.fly();
                        break;
                    case 6:
                        hero.land();
                        break;
                    case 7:
                        hero.fight(); // 子クラスのオーバーライドされた戦うメソッドを呼ぶ
                        break;
                    case 9:
                        hero.endAdventure();
                        return;
                    default:
                        hero.pass();
                }
            }
        }
    }
}