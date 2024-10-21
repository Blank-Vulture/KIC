package period4;

public class Practice7 {

    public static void main(String[] args) {
        // 2次元配列の宣言と初期化
        int[][] numbers = new int[3][3];
        int value = 1;

        // 配列を1から9で初期化
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                numbers[i][j] = value;
                value++;
            }
        }

        // 配列の内容を表示
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(numbers[i][j]);
                if (j < 2) {
                    System.out.print(", "); // カンマ区切り
                }
            }
            System.out.println(); // 改行
        }
    }
}