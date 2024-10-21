package period3;

import java.util.Scanner;

public class Practice4 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("あなたの年齢を入力してください");
		int age = scanner.nextInt();
		if (age < 18) {
			System.out.println("未成年です");
		} else {
			System.out.println("成人です");
		}
		scanner.close();
	}

}
