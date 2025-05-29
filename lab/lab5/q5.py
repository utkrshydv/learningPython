import math


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


r1 = Rectangle(10, 2)
print("Rectangle area:", r1.area())

c1 = Circle(10)
print("Circle area:", c1.area())
