class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __contains__(self, item):
        return item in self.items


inv = Inventory()
inv.add("sword")
inv.add("shield")

print("sword" in inv)    # ✅ True
print("bow" in inv)      # ✅ False


class Scoreboard:
    def __init__(self):
        self.scores = {}

    def __setitem__(self, player, score):
        self.scores[player] = score

    def __getitem__(self, player):
        return self.scores[player]


sb = Scoreboard()
sb["Alice"] = 100
sb["Bob"] = 150

print(sb["Alice"])       # ✅ 100
print(sb["Bob"])         # ✅ 150


class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        print(f"{self.greeting}, {name}!")


Jello = Greeter("Hello")
Jello("Utkarsh")     # ✅ Hello, Utkarsh!
