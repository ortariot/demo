
class Singletone:

    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singletone, cls).__new__(cls)
        return cls._instance
    


s1 = Singletone()
s2 = Singletone()
s1.value = 10


# print(s1.value)
# print(s2.value)

# --------------------------------------------------


class Singletone:

    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singletone, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, value):

        if not hasattr(self, "_init"):
            self.value = value
            self._init = True
    


s1 = Singletone(10)
s2 = Singletone(20)


print(s1.value)
print(s2.value)

print(id(s1))
print(id(s2))
print(id(s2) == id(s1))

