# 課題 14: describe_city() 関数
def describe_city(city, country="日本"):
    print(f"{country}にある{city}")


# デフォルト値を使う
describe_city("神戸")

# 別の国の都市
describe_city("パリ", "フランス")

# 別の国の都市
describe_city("ニューヨーク", "アメリカ")
