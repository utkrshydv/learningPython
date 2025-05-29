class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f'{self.owner} : {self.balance}')


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest):
        super().__init__(owner, balance)
        self.interest = interest/100

    def apply_interest(self):
        self.balance = self.balance + (self.balance * self.interest)
        print(f'new balance: {self.balance}')


a1 = SavingsAccount('utkarsh', 1000, 7)
a1.apply_interest()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f'{self.name} : {self.salary}')


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        print(f'{self.name} : {self.salary} : {self.language}')


class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    def display(self):
        print(f'{self.name},{self.salary},{self.tool}')


e1 = Developer('utkarsh', 2000, 'python')
e1.display()
e2 = Designer('not utkarsh', 3000, 'figma')
e2.display()
