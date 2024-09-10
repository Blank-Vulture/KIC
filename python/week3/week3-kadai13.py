# ユーザーに数字を尋ねる
number = input("数字を入力してください: ")

# 入力を整数に変換してから条件を判定
if int(number) % 10 == 0:
    print(f"{number}は10の倍数です。")
else:
    print(f"{number}は10の倍数ではありません。")