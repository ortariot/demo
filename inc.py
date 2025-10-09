class Wallet:

    def __init__(self, name, amount, email):
        self.__name = name
        self.__amount = amount
        self.email = email

    def show_my_money(self):
      print(self.__amount, self.__name)


# gleb_walley = Wallet(name="Gleb", amount=500, email="test@test.ru")
# print(gleb_walley.__dict__)
# print(gleb_walley._Wallet__name) 

# gleb_walley.show_my_money()


class UnsafeWallet:

    def __init__(self, name, amount, email):
        self._name = name
        self._amount = amount
        self.email = email

    def show_my_money(self):
      print(self._amount, self._name)

gleb_unsafe_walley = UnsafeWallet(name="Gleb", amount=500, email="test@test.ru")
print(gleb_unsafe_walley._name) # Ошибки нет -> private
gleb_unsafe_walley.show_my_money()
