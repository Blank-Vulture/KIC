# 課題 12: make_shirt() 関数
def make_shirt(size, message):
    print(f"シャツのサイズ: {size}, 印刷メッセージ: '{message}'")


# 位置引数で呼び出し
make_shirt("M", "Hello World!")

# キーワード引数で呼び出し
make_shirt(size="L", message="Stay Positive!")
