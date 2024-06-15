class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Buggati", "chiron")
print(my_car.brand)
print(my_car.model)

my_newCar = Car("Tata", "Safari")
print(my_newCar.model)

print(my_newCar.full_name())