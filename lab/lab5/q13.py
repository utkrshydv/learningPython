# # polymorphism

# class Dog:
#     def make_sound(self):
#         print("woof")


# class Cat:
#     def make_sound(self):
#         print("meow")


# class Cow:
#     def make_sound(self):
#         print("mooo")


# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     animal.make_sound()

# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius


# shapes = [Rectangle(5, 4), Circle(3)]
# for shape in shapes:
#     print(f"Area: {shape.area()}")


class Employee:
    def work(self):
        print("employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class Designer(Employee):
    def work(self):
        print("Designer is creatign a layout")


labourers = [Employee(), Designer(), Developer()]
for labour in labourers:
    labour.work()
