class Student:
    # pass
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old")


# s1 = Student("utkarsh", 21)
# print(s1.name, s1.age)
# s1.introduce()

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def details(self):
        print(f"brand: {self.brand}, year: {self.year}")


c1 = Car("Toyota", 2017)
c1.details()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"name: {self.title}, author: {self.author}")


b1 = Book("the way of life", 'anon')
b1.info()


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"balance: {self.balance}")

    def display(self):
        print(f"owner: {self.owner}, balance: {self.balance}")


a1 = Account("utkarsh", 1000)
a1.display()
a1.deposit(2000)
a1.display()


class Rectangle:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def area(self):
        print(f"area is {self.lenght * self.width}")


r1 = Rectangle(5, 3)


class Person:
    def __init__(self, name, city="unknown"):
        self.name = name
        self.city = city

    def show_info(self):
        print(f'{self.name}, {self.city}')


p1 = Person("utkarsh", "kolkata")
p1.show_info()

p2 = Person("not utkarsh")
p2.show_info()
