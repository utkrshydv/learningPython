def find_avg(number):
    return sum(number)/len(number)


num = list(map(int, input("Enter numbers separated by space: ").split(" ")))
print(f"Average: {find_avg(num)}")
