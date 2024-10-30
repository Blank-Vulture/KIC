package period5.Kadai4;
//import period5.Kadai4.Mondai1;
public class Mondai2 {

	public static void main(String[] args) {
		String address = "info@example.com";
		String text = "javaの勉強をしています";
		
		email(address, text);
	}
	
	//emailメソッドをオーバーロード
	//titleは無題
	public static void email(String address, String text) {
	    // importしているperiod5.Kadai4.Mondai1クラスのemailメソッドを呼び出す
		Mondai1.email("無題", address, text);
	}

}
