def find_max_in_list(number):
    max = number[0]
    for num in number:
        if num > max:
            max = num
    return max


def find_max_prebuilt(numbers):
    return max(numbers)


n = list(map(int, input("Enter numbers separated by space: ").split(" ")))
print(f"max: {find_max_in_list(n)}")
print(f"max: {find_max_prebuilt(n)}")
