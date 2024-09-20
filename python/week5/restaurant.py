# restaurant.py
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