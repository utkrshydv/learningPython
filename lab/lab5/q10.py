class Speaker:
    def speak(self):
        print("speaking")


class Mover:
    def move(self):
        print("moving")


class Robot(Speaker, Mover):
    pass


r1 = Robot()
r1.speak()
r1.move()


class A:
    def greet(self):
        print("A")


class B:
    def greet(self):
        print("B")


class C(A, B):
    pass


class D(B, A):
    pass


t1 = C()
t1.greet()
t2 = D()
t2.greet()


class E(A, B):
    def greet(self):
        A.greet(self)
        B.greet(self)
        print("E")


t3 = E()
t3.greet()
