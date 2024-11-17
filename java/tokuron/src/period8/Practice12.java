package period8;
import java.util.Scanner;
public class Practice12 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // 勇者と剣の名前を入力
            System.out.print("勇者の名前を付けて下さい: ");
            String heroName = scanner.nextLine();

            System.out.print("剣の名前を付けて下さい: ");
            String swordName = scanner.nextLine();

            // 剣と勇者のインスタンスを作成
            Practice12Sword sword = new Practice12Sword(swordName);
            Practice12Hero hero = new Practice12Hero(heroName, sword);
            System.out.println("勇者は" + heroName + "と名付けられた");
            System.out.println("剣は" + swordName + "と名付けられた");

            // 指示を出すループ
            while (true) {
                System.out.println("勇者" + heroName + "は冒険に出かけた。指示をしてください。");
                System.out.println("1:戦う 2:逃げる 3:眠る 4:剣で戦う 9:終了");

                int command = scanner.nextInt();

                switch (command) {
                    case 1:
                        hero.fight();
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
                    case 9:
                        hero.endAdventure();
                        break;
                    default:
                        hero.pass();
                        break;
                }
            }
        }
    }
}
