# # encapsulation

# class Person:
#     def __init__(self, name, age):
#         self.name = name  # public
#         self._hobby = "reading"  # protected
#         self.__salary = 50000  # private

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, new_salary):
#         if new_salary > 0:
#             self.__salary = new_salary


# p = Person("alex", 25)
# print(p.name)
# print(p._hobby)
# # print(p.__salary) error

# print(p.get_salary())


# class BankAccount:

#     def __init__(self):
#         self.__balance = 10000

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount < self.__balance:
#             self.__balance -= amount

#     def get_balance(self):
#         print(self.__balance)


# a1 = BankAccount()
# a1.deposit(999)
# a1.withdraw(700)
# a1.get_balance()


class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    def display_marks(self):
        print(f'{self.name} : {self._marks}')


class Topper(Student):
    def boost_marks(self):
        self._marks += 5


s1 = Topper("Anjali", 90)
s1.display_marks()

s1.boost_marks()
s1.display_marks()

print(s1._marks) #should not be used...against the convention
