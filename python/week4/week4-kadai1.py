# 課題 1: ユーザーに名前を尋ね、guest.txtに書き込むプログラム
name = input("あなたの名前を教えてください: ")
filename = "guest.txt"

with open(filename, "w") as file_object:
    file_object.write(f"{name}\n")

print("名前を記録しました")
