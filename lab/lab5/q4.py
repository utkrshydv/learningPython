# inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} makes a sound')


class Dog(Animal):
    def speak(self):
        print(f'{self.name} says woof')


class Cat(Animal):
    def speak(self):
        print(f'{self.name} says Meow')


dog = Dog('Buddy')
cat = Cat('Whiskers')
dog.speak()
cat.speak()


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f'{self.brand}, {self.year}')


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def show_info(self):
        print(f'{self.brand}, {self.year}, {self.model}')


c1 = Car("Toyota", 2017, "Corolla")
c1.show_info()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f'{self.name} : {self.salary}')


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print(f'{self.name} : {self.department} : {self.salary}')


m1 = Manager('utkarsh', 20000, 'standup')
m1.show_info()
