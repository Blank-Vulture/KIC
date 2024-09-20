# admin_privileges.py
from user import User


class Privileges:
    def __init__(self):
        self.privileges = ["記事を追加できる", "記事を削除できる", "ユーザーを管理できる"]

    def show_privileges(self):
        print("管理者の特権:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()
