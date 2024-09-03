# 課題 8

# 任意のリストを作成
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ① スライスを使って、リストにある最初の3つのデータを表示
print("最初の3つのデータ:", numbers[:3])

# ② スライスを使って、リストの真ん中にある3つのデータを表示
middle_index = len(numbers) // 2
print("真ん中の3つのデータ:", numbers[middle_index-1:middle_index+2])

# ③ スライスを使って、リストの最後の3つのデータを表示
print("最後の3つのデータ:", numbers[-3:])

# 課題 9

# ① "my_friends"リストにサイバーパンク：エッジランナーズのキャラクターを追加
my_friends = ["David", "Lucy", "Maine"]
your_friends = my_friends[:]  # リストのコピー

my_friends.append("Rebecca")  # my_friendsに新しい友達を追加

# ② "your_friends"リストに別の名前を追加
your_friends.append("Faraday")  # your_friendsに別の名前を追加

# ③ forループを使って「私の友達は：」というメッセージを表示し、 “my_friends”リストにある名前をprint
print("私の友達は：")
for friend in my_friends:
    print(friend)

# ④ forループを使って「あなたの友達は：」というメッセージを表示し、“your_friends”リストにある名前をprint
print("あなたの友達は：")
for friend in your_friends:
    print(friend)