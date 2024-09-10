# 空のリスト生成
aliens = []

# 30個greenのエイリアンを生成
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 最初の5つのエイリアンを表示
for alien in aliens[:5]:
    print(alien)

print("...")

# 生成されたエイリアンの数を表示
print(f"Total number of aliens: {len(aliens)}")

# エイリアンの最初の3つをアップデート（例: 色を黄色に変更し、ポイントと速度も変更）
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# 使用する武器のリスト
weapons = ['blaster', 'laser', 'plasma gun', 'rocket launcher', 'sniper rifle']

# エイリアンに順番に異なる武器を持たせる
weapon_index = 0
for alien in aliens:
    alien['weapon'] = weapons[weapon_index]
    weapon_index = (weapon_index + 1) % len(weapons)

# 最初の5つのエイリアンの新しい情報を表示
for alien in aliens[:5]:
    print(alien)