# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Student(name='{self.name}', age={self.age})"


# s1 = Student("Utkarsh", 21)
# print(s1)            # Student(name='Utkarsh', age=21)
# print([s1])          # [Student(name='Utkarsh', age=21)]


# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.enrolled = []

#     def add_student(self, student):
#         self.enrolled.append(student)

#     def __repr__(self):
#         return f'{self.name}, {self.enrolled}'

#     def __len__(self):
#         return len(self.enrolled)


# c = Course("Python")
# c.add_student("Alice")
# c.add_student("Bob")
# print(len(c))
# print(c)

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.volume = x*y*z

    def display(self):
        print(self.volume)

    def __lt__(self, other):
        return self.volume < other.volume


b1 = Box(3, 3, 3)
b1.display()
b2 = Box(2, 3, 4)
b2.display()
print(b1 < b2)
print(b2 < b1)


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title):
        self.notes.append(title)

    def __getitem__(self, index):
        return self.notes[index]


n = Notebook()
n.add_note("Buy milk")
n.add_note("Study OOP")

print(n[0])          # Buy milk
print(n[1])          # Study OOP
