from abc import ABC, abstractmethod


# class User(ABC):

#     @abstractmethod
#     def login(self):
#         pass


# class Student(User):
#     def __init__(self, username, passwrd):
#         self.username = username
#         self.___password = passwrd
#         self.enrolled = []

#     def login(self):
#         print(f'{self.username}, your passsword is {self.___password}')

#     def enroll(self, course):
#         self.enrolled.append(course)

#     def display_details(self):
#         print(f'{self.username}, courses: ')
#         for course in self.enrolled:
#             print(course)


# class Instructor(User):
#     def __init__(self, username, passwrd):
#         self.username = username
#         self.__password = passwrd
#         self.courses = []

#     def login(self):
#         print(f'{self.username}, your password is {self.__password}')

#     def create_course(self, course):
#         self.courses.append(course)

#     def display_details(self):
#         print(f'{self.username}, courses created: ')
#         for course in self.courses:
#             print(course)


# s1 = Student("utkarsh", "123456")
# s1.login()
# s1.enroll("maths")
# s1.enroll("english")
# s1.display_details()

# i1 = Instructor("username", "password")
# i1.login()
# i1.create_course('geography')
# i1.create_course('biology')
# i1.display_details()

class Employee(ABC):

    employee_count = 0

    @abstractmethod
    def work(self):
        pass

    @classmethod
    def display_count(cls):
        print(cls.employee_count)


class Manager(Employee):

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    def work(self):
        print("Manager is working")


class Developer(Employee):

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    def work(self):
        print("Developer is working")


class Designer(Employee):

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    def work(self):
        print("Designer is working")


a = Designer("a")
b = Developer("b")
c = Manager("c")

Employee.display_count()
