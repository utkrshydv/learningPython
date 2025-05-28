t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t[0:4])
print(t[7:][::-1])
print(t[1::2])

student = ("utkarsh", (90, 80, 70), ("math", "science", "english"))
print(student[0])
print(student[2][1])
print((student[1][0] + student[1][1] + student[1][2]) / 3)

sum = 0
for i in range(0, 3):
    sum += student[1][i]

print(sum/3)
