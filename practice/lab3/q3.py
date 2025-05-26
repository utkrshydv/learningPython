def find_factorial(num):
    if num == 1:
        return 1
    return num * find_factorial(num-1)


n = int(input("enter number: "))
print(f"The factorial is: {find_factorial(n)}")
