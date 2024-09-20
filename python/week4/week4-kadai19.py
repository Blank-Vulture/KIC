# 事前に作成された build_profile() 関数
def build_profile(first, last, **user_info):
    """ユーザーに関する情報を含む辞書を作成する"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


# プロファイルを構築
my_profile = build_profile("Takaya", "SHIRAISHI", age=23, location="Kamakura", profession="Graduated School Student")

# プロファイルの表示
print("\nあなたのプロファイル:")
for key, value in my_profile.items():
    print(f"{key}: {value}")
