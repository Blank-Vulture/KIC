# 課題12

# エイリアンの色リストを作成
alien_colors = ['green', 'yellow', 'red']

# if-elif-elseのチェーンでポイントを判定
for alien_color in alien_colors:
    if alien_color == 'green':
        print(f"{alien_color.title()}のエイリアン: プレーヤーは5点を獲得しました！")
    elif alien_color == 'yellow':
        print(f"{alien_color.title()}のエイリアン: プレーヤーは10点を獲得しました！")
    elif alien_color == 'red':
        print(f"{alien_color.title()}のエイリアン: プレーヤーは15点を獲得しました！")

# 課題13

# 変数ageに値をセット
age = 25

# if-elif-elseでライフステージを判定
if age < 2:
    print("赤ん坊")
elif age < 4:
    print("幼児")
elif age < 13:
    print("子供")
elif age < 20:
    print("少年")
elif age < 65:
    print("大人")
else:
    print("高齢者")

# 課題14

# 好きな果物をリストに入れる
favorite_fruits = ['バナナ', 'りんご', 'ぶどう']

# 5つのif文で果物がリストに含まれているかをチェック
if 'バナナ' in favorite_fruits:
    print("あなたは本当にバナナが好きなのですね！")

if 'りんご' in favorite_fruits:
    print("あなたは本当にりんごが好きなのですね！")

if 'ぶどう' in favorite_fruits:
    print("あなたは本当にぶどうが好きなのですね！")

if 'オレンジ' in favorite_fruits:
    print("あなたは本当にオレンジが好きなのですね！")

if 'パイナップル' in favorite_fruits:
    print("あなたは本当にパイナップルが好きなのですね！")