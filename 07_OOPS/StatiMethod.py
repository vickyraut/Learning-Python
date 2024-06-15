class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    @staticmethod
    def generalDescription():
        return "Cars are mean to transport..!"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = Car("Buggati", "chiron")
print(my_car.brand)
print(my_car.model)

my_newCar = Car("Tata", "Safari")
print(my_newCar.model)

print(my_newCar.full_name())

# Inheritance
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.full_name())

# static Method
print(Car.generalDescription())
