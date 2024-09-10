# learning_python.txtの内容を読み込み、"Python"を"C"に置き換えて表示
with open("learning_python.txt") as file:
    lines = file.readlines()  # 行をリストに格納

for line in lines:
    modified_line = line.replace("Python", "C")  # 'Python'を'C'に置き換える
    print(modified_line.strip())  # 置き換えた行を表示
