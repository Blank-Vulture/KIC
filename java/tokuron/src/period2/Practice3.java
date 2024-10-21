package period2;

public class Practice3 {

	public static void main(String[] args) {
		// キャストによるデータ破損の確認
		double rawPi = 0.0;

		// ライプニッツの公式で円周率を求める
		for (int i = 1; i < 100000; i++) {
			if (i % 2 == 0) {
				rawPi -= 1.0 / (2 * i - 1);
			} else {
				rawPi += 1.0 / (2 * i - 1);
			}
		}
		rawPi *= 4;

		int droppedPi = (int) rawPi;
		System.out.println("キャスト前(double): "+rawPi);
		System.out.println("キャスト後(int): "+droppedPi);
	}

}
