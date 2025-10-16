

class Books:

    __slots__ = ("title", "author")

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"
    


book = Books("L. Rouling", "Harri Potter")

# print(book.__dict__)


# book.volume = 7
# book.lib = "Lenina Library"

# print(book.volume)
# print(book.lib)



class Pixel:

    __slots__ = ("x", "y")


class OpenPixel(Pixel):
    pass


p = Pixel()

o = OpenPixel()

o.x = 10
o.y = 20
o.color = "black"


print(o.__dict__)

print(o.__slots__)
