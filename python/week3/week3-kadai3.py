# 主要な川とそれぞれの川が流れている国を含む辞書を作成
rivers = {"ナイル川": "エジプト", "アマゾン川": "ブラジル", "長江": "中国"}

# ループを使って、各河川に関する文章を表示
for river, country in rivers.items():
    print(f"{river}は{country}にある川です。")

# ループを使用して、辞書に含まれる各河川の名前を表示
print("\n河川の名前:")
for river in rivers:  # pylintの警告(C0201)により.keys() を省略
    print(river)

# ループを使用して、辞書に含まれるそれぞれの国の名前を表示
print("\n国の名前:")
for country in rivers.values():
    print(country)
