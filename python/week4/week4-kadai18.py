# 課題 18: サンドウィッチに挟む具材を表示する関数
def make_sandwich(*ingredients):
    print("\nあなたのサンドウィッチに挟む具材:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print("サンドウィッチの注文を承りました。\n")

# 関数を3回呼び、異なる具材を指定
make_sandwich('ハム', 'チーズ', 'レタス')
make_sandwich('トマト', 'バジル')
make_sandwich('ベーコン', '卵', 'アボカド', 'マヨネーズ')