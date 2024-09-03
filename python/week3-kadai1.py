# 課題1

character_info = {
    'name': 'デイビッド・マルティネス',
    'age': 17,
    'city': 'ナイトシティ'
}

# 辞書に格納されている各情報を表示
print(f"氏名: {character_info['name']}")
print(f"年齢: {character_info['age']}")
print(f"住んでいる町: {character_info['city']}")


# 課題2
favorite_numbers = {
    'ルーシー': 7,
    'メイン': 13,
    'レベッカ': 9,
    'ファラデー': 5,
    'ドリオ': 3
}

# 各キャラクターの名前と好きな数字を表示
for name, number in favorite_numbers.items():
    print(f"{name}の好きな数字は {number} です。")