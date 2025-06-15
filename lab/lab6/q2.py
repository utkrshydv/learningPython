class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age}yrs old'


s1 = Student("utkarsh", 21)
print(s1)


class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

    def __str__(self):
        return f'{self.amount}'


w1 = Wallet(50)
w2 = Wallet(100)
w3 = w1 + w2
print(w3.amount)
print(w1)
print(w2)
print(w3)


class Book:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return self.title.replace(" ", "").lower() == other.title.replace(" ", "").lower()


b1 = Book("Python 101")
b2 = Book("python 101")
print(b1 == b2)
