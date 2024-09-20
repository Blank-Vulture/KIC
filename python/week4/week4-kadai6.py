# 課題 6: cats.txt と dogs.txt のファイルを読み込み、内容を表示するプログラム
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(f"{filename}の内容:\n{contents}")
    except FileNotFoundError:
        print(f"エラー: {filename} が見つかりません。")