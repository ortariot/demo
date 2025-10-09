class Animal:
    def __init__(self, color, age): # Конструктор класса
      self.age = age
      self.color = color

    def __repr__(self):
      return f"This is Animal with age = {self.age} and color = {self.color}"

    # def __str__(self):
    #   return "Hi!"

    def eat(self):
        print("Я могу есть")

    def sleep(self):
        print("Я могу спать")

    def animal_birthday(self):
      self.age += 1


cat = Animal("black", 2)


print(cat)