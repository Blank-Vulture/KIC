# 課題1の辞書
person1 = {"name": "デイビッド・マルティネス", "age": 17, "city": "ナイトシティ"}

person2 = {"name": "ルーシー", "age": 20, "city": "ジャパンタウン"}

person3 = {"name": "メイン", "age": 35, "city": "サントドミンゴ"}

# すべての辞書をpeopleというリストに格納
people = [person1, person2, person3]

# リストをループさせて、各人の情報を表示
for person in people:
    print(f"氏名: {person['name']}, 年齢: {person['age']}, 住んでいる町: {person['city']}")
