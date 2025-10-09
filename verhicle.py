class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Марка: {self.make}"
        f"\nМодель: {self.model}"
        f"\nГод выпуска: {self.year}"
        f"\nСтоимость: {self.price} руб")

class Airplane(Vehicle):
    def __init__(self, make, model, year, price, capacity):
        super().__init__(make, model, year, price) # Заберём себе реализацию из Vehicle
        self.capacity = capacity

class Submarine(Vehicle):
    def __init__(self, make, model, year, price, max_depth):
        super().__init__(make, model, year, price) # Заберём себе реализацию из Vehicle
        self.max_depth = max_depth

submarine_obj = Submarine(make="Bronco", model="CB35053", year=1993, price="more than you can imagine", max_depth=4000)
airplane_obj = Airplane(make="СУ", model="80", year=1990, price="55000000$", capacity=30)
print(airplane_obj)
print(submarine_obj)

airplane_obj.display_info()
submarine_obj.display_info()