# 課題 3: User クラスの作成
class User:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print("ユーザー情報:")
        print(f"名前: {self.first_name} {self.last_name}")
        print(f"性別: {self.gender}")
        print(f"年齢: {self.age}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}.")

# インスタンスの作成とメソッドの呼び出し
user_1 = User('V', 'Merc', '不明', 27)
user_2 = User('David', 'Martinez', '男性', 18)

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()