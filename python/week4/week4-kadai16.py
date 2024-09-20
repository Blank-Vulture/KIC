# 課題 16: make_album() 関数
def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album


# 3つのアルバムを表す辞書を作成
album1 = make_album("The Beatles", "Abbey Road")
album2 = make_album("Nirvana", "Nevermind")
album3 = make_album("Pink Floyd", "The Dark Side of the Moon", tracks=10)

# アルバムの情報を表示
print(album1)
print(album2)
print(album3)
