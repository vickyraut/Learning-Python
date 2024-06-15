class Car:
    # Constructor
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Disel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"


# my_car = Car("Buggati", "chiron")
# print(my_car.brand)
# print(my_car.model)
#
# my_newCar = Car("Tata", "Safari")
# print(my_newCar.model)
#
# print(my_newCar.full_name())
#
# # Inheritance
# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.full_name())

# my_car = Car("Buggati", "chiron")
# # print(my_car.brand) # Cannot access private members
# print(my_car.get_brand())

buggati = Car("Buggati", "chiron")
safari = ElectricCar("Tata", "Safari", "85kwh")
print(buggati.fuel_type())
print(safari.fuel_type())
