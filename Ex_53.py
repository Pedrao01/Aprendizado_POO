class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f'Title: {self.title} | Author: {self.author}'

    def __repr__(self) -> str:
        return f'Book: (title={self.title!r}, author={self.author!r})'


book1 = Book('A boa sorte', 'Fernando Trías')
book2 = Book('O alquimista', 'Paulo Coelho')

print(book1)
print(book2)

print(repr(book1))
print(repr(book2))
