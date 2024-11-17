package period4.Kadai3;

public class Mondai1 {

    public static void main(String[] args) {
        // 3つの口座残高を格納するint型配列を宣言
        int[] moneyList = {121902, 8302, 55100};

        // for文で配列の要素を1つずつ取り出して表示
        System.out.println("for文での表示:");
        for (int element : moneyList) {
            System.out.println(element);
        }

        // 拡張for文で配列の要素を1つずつ取り出して表示
        System.out.println("拡張for文での表示:");
        for (int money : moneyList) {
            System.out.println(money);
        }
    }
}