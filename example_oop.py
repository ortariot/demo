# class Animal():

#     def say(self):
#         print("I am animal")


class Duck():

    def say(self):
        print("I am Duck")




class Beaver():

    def say(self):
        print("I am Beaver")

    pass


class Duckbill():
    
    def say(self):
        print("I am platipus")



duckbill = Duckbill()
duck = Duck()
beaver = Beaver()




# duckbill.say()
# duck.say() 
# beaver.say()


animals = (duckbill, duck, beaver) 

for animal in animals:
    animal.say()