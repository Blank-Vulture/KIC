# 課題10

# エイリアンの色リストを作成
alien_colors = ['green', 'yellow', 'red']

# エイリアンの色が'green'であるかどうかを判定
for alien_color in alien_colors:
    if alien_color == 'green':
        print(f"{alien_color.title()}のエイリアン: プレーヤーは5点を獲得しました！")  # 'green'の場合にのみ表示


# 課題11
# エイリアンの色リストを作成
alien_colors = ['green', 'yellow', 'red']

# if-elif-elseのチェーンを使ってポイントを判定
for alien_color in alien_colors:
    if alien_color == 'green':
        print(f"{alien_color.title()}のエイリアン: プレーヤーは5点を獲得しました！")  # 'green'の場合
    else:
        print(f"{alien_color.title()}のエイリアン: プレーヤーは10点を獲得しました！")  # 'green'以外の場合