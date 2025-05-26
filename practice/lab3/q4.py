def find_max(a, b, c):
    if a > b and b > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(f"Largest number is: {find_max(5, 6, 7)}")
