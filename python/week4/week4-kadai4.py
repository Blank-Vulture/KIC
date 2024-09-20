# 課題 4: 2つの数値を入力し、それらを足し算するプログラム
try:
    num1 = input("1つ目の数値を入力してください: ")
    num2 = input("2つ目の数値を入力してください: ")
    result = int(num1) + int(num2)
    print(f"結果は: {result}")
except ValueError:
    print("数値を入力してください。")
