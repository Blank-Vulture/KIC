package period6.practice10.main;
import java.util.Scanner;

import period6.practice10.voice.Voice;
public class Main {

    public static void main(String[] args) {
        boolean[] loop = {true};
        Scanner scanner = new Scanner(System.in);

        while (loop[0]) {
            System.out.println("どの動物の鳴き声が聞きたいですか？ 犬:1, 猫:2, 虎:3, 終了:4");
            int input = scanner.nextInt();

            // Voiceクラスのメソッドを呼び出して鳴き声を取得
            String result = Voice.getAnimalSound(input, loop);
            System.out.println(result);
        }

        scanner.close();
    }

}
