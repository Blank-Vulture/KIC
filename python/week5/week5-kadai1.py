# 課題 1: Restaurant クラスの作成
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"レストラン名: {self.restaurant_name}")
        print(f"料理の種類: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


# インスタンスの作成とメソッドの呼び出し
restaurant = Restaurant("Afterlife Diner", "Street Food")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
