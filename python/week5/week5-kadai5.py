# 課題 5: User クラスの拡張
class User:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0  # デフォルト値を0に設定

    def describe_user(self):
        print("ユーザー情報:")
        print(f"名前: {self.first_name} {self.last_name}")
        print(f"性別: {self.gender}")
        print(f"年齢: {self.age}")
        print(f"ログイン試行回数: {self.login_attempts}")

    def greet_user(self):
        print(f"こんにちは、{self.first_name}さん！")

    # ログイン試行回数を増加させるメソッド
    def increment_login_attempts(self):
        self.login_attempts += 1

    # ログイン試行回数をリセットするメソッド
    def reset_login_attempts(self):
        self.login_attempts = 0

# インスタンスの作成
user = User('David', 'Martinez', '男性', 18)

# ログイン試行を数回行う
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# ログイン試行回数を表示
user.describe_user()

# ログイン試行回数をリセット
user.reset_login_attempts()

# 再度ログイン試行回数を表示
user.describe_user()