from abc import ABC, abstractmethod

class Animals(ABC):

    @abstractmethod
    def say(self):
        pass



class Cat(Animals):

    def myau(self):
        print("Myau")

    def say(self):
        print("I am cat")

cat = Cat()
cat.myau()
cat.say()

