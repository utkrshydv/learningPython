class CustomNotebook:
    def __init__(self):
        self.notes = {}

    def __setitem__(self, title, data):
        self.notes[title] = data

    def __contains__(self, title):
        return title in self.notes

    def __getitem__(self, title):
        return self.notes[title]


n = CustomNotebook()
n["hey"] = "hello world"

print("hey" in n)
print("nay" in n)

print(n["hey"])


class Multiplier:

    def __init__(self, number):
        self.number = number

    def __call__(self, num2):
        print(num2 * self.number)


mul = Multiplier(10)
mul(5)

mul2 = Multiplier(100)
mul2(5)
