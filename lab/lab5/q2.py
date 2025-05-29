class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            print(self.balance)
            self.balance -= amount
            print(self.balance)


a1 = Account(2000)
a1.withdraw(1000)
a1.withdraw(2000)


class Student:
    def __init__(self, name):
        self.name = name
        self.grade = []

    def add_grade(self, grade):
        self.grade.append(grade)

    def average(self):
        if self.grade:
            return sum(self.grade)/len(self.grade)
        else:
            return 0


s1 = Student("utkarsh")
s1.add_grade(90)
s1.add_grade(70)
s1.add_grade(80)
print(f'{s1.name}, {s1.average()}')


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'{book.title} added to the library')

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Borrowed: {book.title} by {book.author}')
                return book
        print("book not found")
        return None


# Create some books
b1 = Book("1984", "George Orwell")
b2 = Book("To Kill a Mockingbird", "Harper Lee")

# Create a library and add books
lib = Library()
lib.add_book(b1)
lib.add_book(b2)

# Try borrowing books
lib.borrow_book("1984")         # Success
lib.borrow_book("The Hobbit")   # Not found
