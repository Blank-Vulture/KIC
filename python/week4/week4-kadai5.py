# 課題 5: 数値が正しく入力されるまで、入力を続けるプログラム
while True:
    try:
        num1 = input("1つ目の数値を入力してください（終了するには'q'を入力してください）: ")
        if num1 == 'q':
            break
        num2 = input("2つ目の数値を入力してください（終了するには'q'を入力してください）: ")
        if num2 == 'q':
            break
        result = int(num1) + int(num2)
        print(f"結果は: {result}")
    except ValueError:
        print("無効な入力です。数値を入力してください。")