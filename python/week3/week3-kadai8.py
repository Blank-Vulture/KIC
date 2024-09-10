# 友達が複数の好きな数字を持てるように辞書を修正
favorite_numbers = {
    'ルーシー': [7, 14, 21],
    'メイン': [13, 26],
    'レベッカ': [9, 18],
    'ファラデー': [5, 10],
    'ドリオ': [3, 6, 9]
}

# 各人の名前と好きな数字を表示
for name, numbers in favorite_numbers.items():
    print(f"{name}さんの好きな数字は:")
    for number in numbers:
        print(f" - {number}")