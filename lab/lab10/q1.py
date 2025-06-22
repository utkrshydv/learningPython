# GENERATORS

def my_generator():
    for i in range(5):
        yield i


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


for j in gen:
    print(j)


def count_upto(n):
    count = 1
    while count <= n:
        yield count
        count += 1


gen = count_upto(10)

for num in gen:
    print(num)


squares = (x*x for x in range(5))

print(squares)

for sq in squares:
    print(sq)


# def read_large_file(filename):
#     with open(filename, 'r') as f:
#         for line in f:
#             yield line.strip()

# # Usage
# for line in read_large_file("mybigfile.txt"):
#     print(line)

# ITERATORS


# nums = [1, 2, 3]

# it = iter(nums)
# print(it)

# print(next(it))
# print(next(it))


# class Counter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= self.limit:
#             num = self.current
#             self.current += 1
#             return num
#         else:
#             raise StopIteration


# c = Counter(3)
# for i in c:
#     print(i)

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            num = self.current
            self.current += 2
            return num
        else:
            raise StopIteration


e = EvenNumbers(100)
for i in e:
    print(i)
