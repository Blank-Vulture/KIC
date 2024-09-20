# 課題 4: Restaurant クラスの拡張
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # デフォルト値を0に設定

    def describe_restaurant(self):
        print(f"レストラン名: {self.restaurant_name}")
        print(f"料理の種類: {self.cuisine_type}")
        print(f"これまでに来られた顧客数: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} は現在営業中です。")

    # 顧客数を設定するメソッド
    def set_number_served(self, number):
        self.number_served = number

    # 顧客数を増やすメソッド
    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers


# インスタンスの作成
restaurant = Restaurant("Afterlife Diner", "Street Food")

# 初期の顧客数を表示
restaurant.describe_restaurant()

# 顧客数を変更して再表示
restaurant.set_number_served(10)
restaurant.describe_restaurant()

# 顧客数を増加させて再表示
restaurant.increment_number_served(5)
restaurant.describe_restaurant()
