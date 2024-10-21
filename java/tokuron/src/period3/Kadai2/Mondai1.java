package period3.Kadai2;

public class Mondai1 {

    public static void main(String[] args) {
        // 1. int型の変数isHungryを定義し、任意で0か1を代入する
        int isHungry = 1;
        //    String型の変数foodを定義し、適当な食べものの名前を代入する
        String food = "おにぎり";

        // 2. 画面に「こんにちは」と表示する
        System.out.println("こんにちは");

        // 3. もし変数isHungryが0であれば「お腹がいっぱいです」、そうでなければ「はらぺこです」と表示する
        if (isHungry == 0) {
            System.out.println("お腹がいっぱいです");
        } else {
            System.out.println("はらぺこです");
        }

        // 4. もしisHungryが空腹を示すならば、変数foodを利用して「○○をいただきます」と表示する
        if (isHungry == 1) {
            System.out.println(food + "をいただきます");
        }

        // 5. 最後に「ごちそうさまでした」と表示する
        System.out.println("ごちそうさまでした");
    }

}
