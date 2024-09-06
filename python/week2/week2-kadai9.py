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