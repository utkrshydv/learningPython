class TaskManager:

    def __init__(self):
        self.tasks = {}

    def __setitem__(self, name, description):
        self.tasks[name] = description

    def __getitem__(self, name):
        return self.tasks[name]

    def __contains__(self, name):
        return name in self.tasks

    def __len__(self):
        return len(self.tasks)

    def __str__(self):
        return f"task manager : {self.tasks}"

    def __repr__(self):
        return f"task manager : {self.tasks}"

    def __call__(self):
        for key in self.tasks:
            print(f"{key} : {self.tasks[key]}")


tm = TaskManager()

tm["laundry"] = "Wash and fold clothes"
tm["study"] = "Study Python OOP"

print("laundry" in tm)     # True
print(tm["study"])         # Study Python OOP

print(len(tm))             # 2

tm()                       # Calls __call__ to print all tasks

print(tm)
print(repr(tm))
