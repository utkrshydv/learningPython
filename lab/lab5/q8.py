# class Book:
#     book_count = 0

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.book_count += 1

#     @classmethod
#     def display_count(cls):
#         print(cls.book_count)


# b1 = Book("abc", "xyz")
# b2 = Book("djbds", "dkjdkjd")
# b1.display_count()
# Book.display_count()
# b2.display_count()


# class Counter:
#     counter = 0

#     def __init__(self):
#         Counter.counter += 1

#     @classmethod
#     def get_total(cls):
#         print(cls.counter)


# c1 = Counter()
# Counter.get_total()
# c2 = Counter()
# Counter.get_total()
# c3 = Counter()
# Counter.get_total()

class Book:
    total_revenue = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def sell(self):
        Book.total_revenue += self.price


b1 = Book("Python 101", 50)
b2 = Book("OOP Mastery", 60)

b1.sell()
b2.sell()

print(Book.total_revenue)  # Output: 110
