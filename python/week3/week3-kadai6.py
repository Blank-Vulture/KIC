# ペットを表す辞書を作成
pet1 = {
    'type': '犬',
    'owner': 'デイビッド'
}

pet2 = {
    'type': '猫',
    'owner': 'ルーシー'
}

pet3 = {
    'type': '鳥',
    'owner': 'メイン'
}

# 辞書をpetsというリストに格納
pets = [pet1, pet2, pet3]

# リストをループして、各ペットについてのデータを表示
for pet in pets:
    print(f"種類: {pet['type']}, 飼い主: {pet['owner']}")