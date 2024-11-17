package period10.Practice16;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // 各キャラクターのインスタンスを生成
            Hero hero = new Hero("アーサー");
            Wizard wizard = new Wizard("ガンダルフ");
            Werewolf wolfman = new Werewolf("フェンリル");

            while (true) {
                System.out.println("誰に指示を出しますか? 1:勇者 2:魔法使い 3:狼男 9:終了");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1:
                        characterAction(hero, scanner, "勇者");
                        break;
                    case 2:
                        characterAction(wizard, scanner, "魔法使い");
                        break;
                    case 3:
                        WerewolfAction(wolfman, scanner);
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

    private static void characterAction(Human character, Scanner scanner, String characterType) {
        while (true) {
            System.out.println(characterType + character.name + "に、指示を出してください。");
            System.out.println("1:歩く 2:逃げる 3:話す 4:休む 5:戦う 9:キャラを変える");
            int command = scanner.nextInt();

            switch (command) {
                case 1:
                    character.walk();
                    break;
                case 2:
                    character.run();
                    break;
                case 3:
                    character.talk();
                    break;
                case 4:
                    character.sleep();
                    break;
                case 5:
                    character.attack();
                    break;
                case 9:
                    return;
                default:
                    System.out.println("正しい数字を入力してください。");
            }
        }
    }

    private static void WerewolfAction(Werewolf wolfman, Scanner scanner) {
        while (true) {
            System.out.println("狼男" + wolfman.name + "に、指示を出してください。");
            System.out.println("1:歩く 2:逃げる 3:話す 4:休む 5:戦う 6:吠える 9:キャラを変える");
            int command = scanner.nextInt();

            switch (command) {
                case 1:
                    wolfman.walk();
                    break;
                case 2:
                    wolfman.run();
                    break;
                case 3:
                    wolfman.talk();
                    break;
                case 4:
                    wolfman.sleep();
                    break;
                case 5:
                    wolfman.attack();
                    break;
                case 6:
                    wolfman.howl();
                    break;
                case 9:
                    return;
                default:
                    System.out.println("正しい数字を入力してください。");
            }
        }
    }
}
