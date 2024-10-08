# 課題 7: Admin クラスの作成
class User:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"ユーザー情報: {self.first_name} {self.last_name}, {self.gender}, {self.age}")

    def greet_user(self):
        print(f"こんにちは、{self.first_name}さん！")


class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ["記事を追加できる", "記事を削除できる", "ユーザーを管理できる"]

    def show_privileges(self):
        print("管理者の特権:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Adminのインスタンスを作成
admin = Admin("Judy", "Alvarez", "女性", 28)
admin.describe_user()
admin.show_privileges()
