def count_even(number):
    count = 0
    for num in number:
        if num % 2 == 0:
            count += 1

    return count


num = list(map(int, input("Enter numbers: ").split(" ")))
print(f"even : {count_even(num)}")
