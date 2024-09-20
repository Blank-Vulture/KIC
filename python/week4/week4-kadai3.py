# 課題 3: プログラミングが好きな理由を尋ね、理由をファイルに記録する
filename = "reasons.txt"

while True:
    reason = input("なぜプログラミングが好きなのですか？（終了するには何も入力せずにエンターを押してください）: ")
    if reason == "":
        break

    with open(filename, "a") as file_object:
        file_object.write(f"{reason}\n")

    print("理由をreasons.txtに保存しました。")
