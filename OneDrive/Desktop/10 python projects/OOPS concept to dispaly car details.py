class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.price)
        print("====================")

# Creating objects of Car class
car1 = Car("Toyota", "Camry", 2022, "$24,970")
car2 = Car("Honda", "Accord", 2022, "$25,935")
car3 = Car("Ford", "Mustang", 2022, "$27,205")

# Displaying information about the cars
print("Car 1:")
car1.display_info()
print("\nCar 2:")
car2.display_info()
print("\nCar 3:")
car3.display_info()
