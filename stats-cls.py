from __future__ import annotations
from typing import NoReturn


class Book:
    def __init__(self, title: str, author: str) -> NoReturn:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.author - self.title}"

    @classmethod
    def from_string(cls, input_string: str) -> Book:
        title, author = input_string.split(" - ")
        return cls(title, author)

    @staticmethod
    def in_isbn(input: str) -> bool:
        return len(input) == 13


book = Book("Harry Potter", "J. Rouling")

new_book = book.from_string("A - B")

print(Book.in_isbn("123"))
