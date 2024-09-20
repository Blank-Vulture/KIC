# 課題 1: Restaurant クラスの作成
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"レストラン名: {self.restaurant_name}")
        print(f"料理の種類: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open! Stay safe out there in the city...")


# 課題 2: 3つの異なるインスタンスの作成
restaurant_1 = Restaurant("El Coyote Cojo", "Mexican")
restaurant_2 = Restaurant("Tom's Diner", "American")
restaurant_3 = Restaurant("Moxie Lounge", "Fusion")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
