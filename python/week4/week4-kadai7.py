# 課題 7: ファイルが見つからなくてもエラーを表示しないようにするプログラム
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(f"{filename}の内容:\n{contents}")
    except FileNotFoundError:
        # ファイルが見つからない場合はエラーを無視
        pass