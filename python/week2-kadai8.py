# 任意のリストを作成
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ① スライスを使って、リストにある最初の3つのデータを表示
print("最初の3つのデータ:", numbers[:3])

# ② スライスを使って、リストの真ん中にある3つのデータを表示
middle_index = len(numbers) // 2
print("真ん中の3つのデータ:", numbers[middle_index-1:middle_index+2])

# ③ スライスを使って、リストの最後の3つのデータを表示
print("最後の3つのデータ:", numbers[-3:])