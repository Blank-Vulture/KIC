# user.py
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
