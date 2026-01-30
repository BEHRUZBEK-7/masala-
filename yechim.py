
# class CartItem:
#     def __init__(self, name, price, quantity, discount):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.discount = discount
#
#     def total_cost(self):
#         return self.price * self.quantity * (1 - self.discount / 100)
#
#
# class FoodItem(CartItem):
#     def total_cost(self):
#         cost = super().total_cost()
#         return f"Oziq-ovqat: {self.name} | Jami narx: ${cost:.2f}"
#
#
# class NonFoodItem(CartItem):
#     def total_cost(self):
#         cost = super().total_cost()
#         return f"Nooziq-ovqat: {self.name} | Jami narx: ${cost:.2f}"
#
# items = [
#     FoodItem("Olma", 1.5, 3, 10),
#     FoodItem("Non", 2.0, 2, 5)
# ]
#
# for item in items:
#     print(item.total_cost())
#
# class Vehicle:
#     def __init__(self, name, distance, fuel_efficiency, fuel_price):
#         self.name = name
#         self.distance = distance
#         self.fuel_efficiency = fuel_efficiency
#         self.fuel_price = fuel_price
#
#     def trip_cost(self):
#         return self.distance * self.fuel_efficiency * self.fuel_price
# class Car(Vehicle):
#     def trip_cost(self):
#         cost = super().trip_cost()
#         return f"Avtomobil ({self.name}) | Xarajat: ${cost:.2f}"
# class Motorcycle(Vehicle):
#     def trip_cost(self):
#         cost = super().trip_cost()
#         return f"Motosikl ({self.name}) | Xarajat: ${cost:.2f}"
# vehicles = [
#     Car("Avto", 100, 0.1, 1.5),
#     Motorcycle("Motosikl", 50, 0.05, 1.5)
# ]
# for vehicle in vehicles:
#     print(vehicle.trip_cost())


class pet:
    def __init__(self,name, dailing_food):
        self.name=name
        self.dailing_food=dailing_food
    def feeding_plan(self):
        return self.dailing_food
class dog(pet):
    def __init__(self,name,dailing_food):
        super().__init__(name,dailing_food)
class cat(pet):
    def __init__(self,name,dailing_food):
        super().__init__(name,dailing_food)
dog = dog("Dog",1)
cat = cat("Cat",1)


class Order :
    def __init__(self, name , price, service_fee ) :
        self.price = price
        self.service_fee = service_fee
        self.name = name
    def total_cost(self):
        return self.price * self.service_fee
class Service(Order) :
    def __init__(self, name, price, service_fee ) :
        Order.__init__(self, name, price, service_fee)
class MainDish(Order) :
    def __init__(self, name, price, service_fee ) :
        Order.__init__(self, name, price, service_fee)
class SideDish(Order) :
    def __init__(self, name, price, service_fee ) :
        Order.__init__(self, name, price, service_fee)
MainDish = MainDish("Main Dish",1,1)