# 課題 6: IceCreamStand クラスの作成
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"レストラン名: {self.restaurant_name}")
        print(f"料理の種類: {self.cuisine_type}")
        print(f"これまでに来られた顧客数: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} は現在営業中です。")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry']

    def show_flavors(self):
        print("提供中のアイスクリームの種類:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# IceCreamStandのインスタンスを作成
ice_cream_stand = IceCreamStand('Sweet Treats')
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()