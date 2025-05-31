# # multiple inheritance

# class ClassA:
#     def method_a(self):
#         print("Method A")


# class ClassB:
#     def method_b(self):
#         print("Method B")


# class Child(ClassA, ClassB):
#     pass


# c = Child()
# c.method_a()
# c.method_b()

# #Python uses Method Resolution Order (MRO) to decide which method to call — it goes left to right based on the order of inheritance.

class A:
    def greet(self):
        print("Hello from A")


class B:
    def greet(self):
        print("Hello from B")


class C(A, B):
    pass


c = C()
c.greet()


print(C.mro())
# Or
print(C.__mro__)
