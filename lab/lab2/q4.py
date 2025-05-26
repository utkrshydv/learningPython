a, b, c = input("Enter three numbers: ").split(", ")

a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print(f"{a} is the largest")
elif b > a and b > c:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")
