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