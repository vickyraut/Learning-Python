class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("Buggati", "chiron")
print(my_car.brand)
print(my_car.model)

my_newCar = Car("Tata", "Safari")
print(my_newCar.model)