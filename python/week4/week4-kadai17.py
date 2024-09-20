# 課題 17: whileループでユーザー入力を受け取るプログラム
def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


while True:
    print("\nアルバムのアーティストとタイトルを入力してください:")
    print("(終了するには 'q' を入力してください)")

    artist = input("アーティスト名: ")
    if artist == 'q':
        break

    title = input("アルバムタイトル: ")
    if title == 'q':
        break

    tracks = input("曲数 (任意の項目、入力しない場合は空欄のまま): ")
    if tracks == 'q':
        break
    elif tracks:
        album = make_album(artist, title, tracks=int(tracks))
    else:
        album = make_album(artist, title)

    print(f"\n作成されたアルバム: {album}")