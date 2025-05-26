def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


n = int(input("Enter a number: "))
print("THe number is ", even_odd(n))
