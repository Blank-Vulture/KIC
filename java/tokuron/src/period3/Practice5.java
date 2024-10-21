package period3;

import java.util.Random;
import java.util.Scanner;

public class Practice5 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int select = 0;
		int omikuji = 0;
		int destiny = 0;
		String result = "";

        while(true) {
        	System.out.println("おみくじを引きますか？　Yes:1を入力 No:2を入力");
        	select = scanner.nextInt();
			if (select != 1 && select != 2) {
				System.out.println("正しい文字を入力してください");
				continue;
			}
        	if(select == 2) {
        		System.out.println("終了します");
        		break;
        	}
        	if (select == 1) {
        		omikuji = new Random().nextInt();
        		destiny = omikuji % 5;
        		switch(destiny) {
				case 0:
					result = "大吉";
				case 1:
					result = "中吉";
				case 2:
					result = "小吉";
				case 3:
					result = "吉";
				case 4:
					result = "凶";
        		}
        		System.out.println("あなたの運命数は"+omikuji+"です。"+"運勢は"+result+"です");
        	}
        }

		scanner.close();
	}

}
