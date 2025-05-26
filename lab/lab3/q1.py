def add_numbers(a, b):
  return a+b

x, y = input("Enter two numbers: ").split(", ")

print("Sum: ", add_numbers(int(x), int(y)))