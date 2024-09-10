# 課題 14: learning_python.txt の内容を3つの方法で表示
# ファイル全体を読み込んで表示する
with open('learning_python.txt') as file:
    contents = file.read()
    print(contents)

# ファイルオブジェクトをループして表示する
with open('learning_python.txt') as file:
    for line in file:
        print(line.strip())  # strip()を使って末尾の改行を削除して表示

# 行をリストに格納してwithブロックの外で操作して表示する
with open('learning_python.txt') as file:
    lines = file.readlines()  # 行をリストに格納

for line in lines:
    print(line.strip())  # strip()を使って末尾の改行を削除して表示