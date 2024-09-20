# 課題 13: デフォルト値を設定した make_shirt() 関数
def make_shirt(size='L', message='I love Python'):
    print(f"シャツのサイズ: {size}, 印刷メッセージ: '{message}'")

# Lサイズのシャツ（デフォルトのメッセージ）
make_shirt()

# Mサイズのシャツ（デフォルトのメッセージ）
make_shirt('M')

# 任意のサイズのシャツ（別のメッセージ）
make_shirt('S', 'Code is life')