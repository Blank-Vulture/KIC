import json

# ユーザーから好きな番号を入力させる
favorite_number = input("あなたの好きな番号を入力してください: ")

# 好きな番号をファイルに保存する
filename = "favorite_number.json"
with open(filename, "w") as file_object:
    json.dump(favorite_number, file_object)

print(f"あなたの好きな番号を {favorite_number} として保存しました。")
