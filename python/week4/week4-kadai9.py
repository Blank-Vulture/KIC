import json

filename = 'favorite_number.json'

# 好きな番号を保存したファイルがあるか確認し、表示する
try:
    with open(filename) as file_object:
        favorite_number = json.load(file_object)
    print(f"あなたの好きな番号を知っています！それは {favorite_number} です。")
except FileNotFoundError:
    # ファイルがない場合、ユーザーに好きな番号を入力させ、それを保存する
    favorite_number = input("あなたの好きな番号を入力してください: ")
    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)
    print(f"あなたの好きな番号を {favorite_number} として保存しました。")