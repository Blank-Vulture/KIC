package period5.Kadai4;

public class Mondai1 {

	public static void main(String[] args) {
		String title = "お知らせ";
		String address = "info@example.com";
		String text = "新しい情報です";

		email(title, address, text);

	}

	//emailメソッドを定義
	//戻り値：なし
	//引数：String title, String address, String text
	//処理：以下の形式で表示を行う
	// メールの宛先アドレス(address)に、以下のメールを送信しました
	// 件名：title
	// 本文：text
	public static void email(String title, String address, String text) {
		System.out.println(address + "に、以下のメールを送信しました");
		System.out.println("件名：" + title);
		System.out.println("本文：" + text);
	}

}
