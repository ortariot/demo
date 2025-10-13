from random import choice

class SomeClass:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print("Start constructor")
        return instance

    def __init__(self, val):
        print("init")
        self.val = val



# my_class = SomeClass(10)


class Dog:
    def say(self):
        print("I am Dog")

class Cat:
    def say(self):
        print("I am Cat")

class Fox:
    def say(self):
        print("I am Fox")


class Animals:

    def __new__(cls):
        other = choice([Dog, Cat, Fox])

        instance = super().__new__(other)

        print(f"I am {type(instance).__name__}")

        return instance

    def __init__(self):
        pass


if __name__ == "__main__":
    pet = Animals()

