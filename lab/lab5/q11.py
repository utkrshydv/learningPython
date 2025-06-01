from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * self.radius * self.radius)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)


c1 = Circle(10)
c1.area()
r1 = Rectangle(10, 10)
r1.area()


class MediaFile(ABC):

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def play(self):
        pass


class AudioFile(MediaFile):

    def play(self):
        print(f"playing audiofile: {self.filename}")


class VideoFile(MediaFile):

    def play(self):
        print(f'playing video file : {self.filename}')


audio = AudioFile("song.mp3")
audio.play()

video = VideoFile("video.mp4")
video.play()


class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    def __init__(self, name, salary, prog_lang):
        super().__init__(name, salary)
        self.prog_lang = prog_lang

    def work(self):
        print(f'{self.name} : {self.salary} : {self.prog_lang}')


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        print(f'{self.name} : {self.salary} : {self.team_size}')


d1 = Developer("utkarsh", 200000, "java")
d1.work()
m1 = Manager("utkkk", 300000, 45)
m1.work()


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print('car starts')

    def stop_engine(self):
        print('car stops')


class Bike(Vehicle):
    def start_engine(self):
        print('bike starts')

    def stop_engine(self):
        print('bike stops')


car1 = Car()
car1.start_engine()
car1.stop_engine()

bike1 = Bike()
bike1.start_engine()
bike1.stop_engine()


class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def calculate_interest(self):
        print(f'{0.05 * self.balance: .2f}')


class FixedDepositAccount(Account):
    def calculate_interest(self):
        print(f'{0.07 * self.balance:.2f}')


s1 = SavingsAccount(10000)
s1.calculate_interest()

f1 = FixedDepositAccount(10000)
f1.calculate_interest()
