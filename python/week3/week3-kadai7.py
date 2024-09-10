# favorite_placesという辞書を作成
favorite_places = {
    'デイビッド': ['アフターライフ', 'サントドミンゴ'],
    'ルーシー': ['ナイトシティスカイライン', 'ジャパンタウン'],
    'メイン': ['ヘイウッド', 'ノースサイド']
}

# 辞書をループして、各人の名前と好きな場所を表示
for name, places in favorite_places.items():
    print(f"{name}さんのお気に入りの場所は:")
    for place in places:
        print(f" - {place}")