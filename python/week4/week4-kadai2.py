# 課題 2: 名前を入力させて、guest_book.txtに記録し、挨拶を表示する
filename = "guest_book.txt"

while True:
    name = input("あなたの名前を教えてください（終了するには何も入力せずにエンターを押してください）: ")

    # 終了条件：入力が空の場合、ループを終了
    if name == "":
        break

    print(f"こんにちは、{name}さん")

    with open(filename, "a") as file_object:
        file_object.write(f"{name}\n")

    print(f"{name}さんの名前をguest_book.txtに記録しました。")
