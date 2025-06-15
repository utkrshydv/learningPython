# dunder methods
# | Method     | Purpose                                       |
# | ---------- | --------------------------------------------- |
# | `__init__` | Constructor (called when object is created)   |
# | `__str__`  | Defines what `print(obj)` or `str(obj)` shows |
# | `__repr__` | Official string representation for debugging  |
# | `__eq__`   | Custom logic for `==` comparison              |
# | `__add__`  | Custom logic for `+` operator                 |
# | `__len__`  | Custom logic for `len(obj)`                   |

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'


b1 = Book("1984", "George Orwell")
print(b1)  # Output: "1984" by George Orwell


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)  # Output: Point(6, 8)


class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


p1 = Person("Alice")
p2 = Person("alice")
print(p1 == p2)  # Output: True
