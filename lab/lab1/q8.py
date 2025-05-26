name, sub1, sub2, sub3 = input("Enter name and marks: ").split(", ")

avg = (float(sub1) + float(sub2) + float(sub3))/3

if avg >= 40:
    print(f"{name} passed")
else:
    print(f"{name} failed")
