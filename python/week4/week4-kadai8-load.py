import json

# 好きな番号をファイルから読み込む
filename = 'favorite_number.json'
try:
    with open(filename) as file_object:
        favorite_number = json.load(file_object)
    print(f"あなたの好きな番号を知っています！それは {favorite_number} です。")
except FileNotFoundError:
    print("好きな番号がまだ保存されていません。")