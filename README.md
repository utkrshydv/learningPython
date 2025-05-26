# **learningPython**




## Lab 1

### Topic: Basic Input/Output & f-strings

**Explanation:**
Python’s built-in `input()` function reads a line of text from the user as a string. To display output, you can use `print()`. f-strings (`f"…{expr}…"`) let you embed expressions directly inside string literals for readable formatting.

**Example:**

```python
name = input("Enter your name: ")
age  = input("Enter your age: ")
print(f"Hello {name}. You're {age} years old")
```

**Questions I have done on that topic:**

* Question 1: Greeted the user by name and age using `input()` and an f-string.

---

### Topic: Type Conversion & Addition

**Explanation:**
User input is always a string. To perform numeric operations, convert with `int()` or `float()`. You can then add mixed types (e.g. `int + float`) and Python will promote to the more general `float`.

**Example:**

```python
num1  = int(input("Enter a number: "))
num2  = float(input("Enter a float: "))
total = num1 + num2
print(f"The sum is: {total}")
```

**Questions I have done on that topic:**

* Question 2: Converted inputs to `int` and `float`, then printed their sum.

---

### Topic: Arithmetic Operators

**Explanation:**
Python supports the usual arithmetic operators:

* `+` (addition)
* `-` (subtraction)
* `*` (multiplication)
* `/` (true division)
* `//` (floor division)
* `%` (modulus)
* `**` (exponentiation)

**Example:**

```python
a = 10
b =  3
print("Addition:       ", a + b)
print("Subtraction:    ", a - b)
print("Multiplication: ", a * b)
print("Division:       ", a / b)
print("Floor Division: ", a // b)
print("Modulus:        ", a % b)
print("Exponentiation: ", a ** b)
```

**Questions I have done on that topic:**

* Question 3: Demonstrated all basic arithmetic operators with `a = 10` and `b = 3`.

---

### Topic: String Splitting & Multiple Assignment

**Explanation:**
The string method `.split(sep)` breaks a string into a list by the given separator. You can then unpack those list elements directly into multiple variables in one line.

**Example:**

```python
name, age, score = input("Enter name, age and score: ").split(", ")
print(f"name: {name}, age: {age}, score: {score}")
```

**Questions I have done on that topic:**

* Question 4: Read three comma-separated values and assigned them to `name`, `age`, and `score`.

---

### Topic: Converting & Concatenating Numeric Strings

**Explanation:**
You can convert string representations of numbers back to numeric types (`int`, `float`), do arithmetic, and then convert back to strings for concatenation.

**Example:**

```python
int_str   = int(input("Enter integer as string: "))
float_str = float(input("Enter float as string: "))

print(int_str, float_str)                  # numeric output
print(int_str + float_str)                # arithmetic sum
print(str(int_str) + str(float_str))      # string concatenation
```

**Questions I have done on that topic:**

* Question 5: Converted inputs from strings to numbers, then demonstrated both arithmetic addition and string concatenation.

---

### Topic: Conditional Statements

**Explanation:**
Use `if`, `else` (and optionally `elif`) to execute code blocks based on boolean conditions.

**Example:**

```python
marks = float(input("Enter your marks: "))
if marks >= 40:
    print("Passed")
else:
    print("Failed")
```

**Questions I have done on that topic:**

* Question 6: Checked pass/fail status based on a single `marks` input.

---

### Topic: Calculating Percentage & Average

**Explanation:**
You can perform compound arithmetic expressions to compute percentages and averages:

* **Percentage** = `(sum of marks) / (total maximum) * 100`
* **Average** = `(sum of marks) / (number of subjects)`

**Examples:**

```python
# Percentage
subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))
percentage = ((subject1 + subject2 + subject3) / 300) * 100
print(f"Percentage: {percentage}")

# Average with conditional pass/fail
name, sub1, sub2, sub3 = input("Enter name and marks: ").split(", ")
avg = (float(sub1) + float(sub2) + float(sub3)) / 3
if avg >= 40:
    print(f"{name} passed")
else:
    print(f"{name} failed")
```

**Questions I have done on that topic:**

* Question 7: Calculated percentage from three subject marks.
* Question 8: Computed average of three marks and used a conditional to print pass/fail.

---


## Lab 2

### Topic: Random Number Guessing Game

**Explanation:**
This program uses the `random` module to generate a secret integer between 1 and 10. A `while True` loop repeatedly prompts the user to guess; based on the comparison, it prints hints ("guess higher"/"guess lower") until the correct number is guessed, then breaks out of the loop.

**Example:**

```python
import random
number_to_guess = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number_to_guess:
        print("guess higher")
        continue
    elif guess > number_to_guess:
        print("guess lower")
        continue
    else:
        print("Correct!")
        break
```

**Questions I have done on that topic:**

* Question 1: Built a guessing game that loops until the user finds the randomly chosen number, using `continue` and `break`.

---

### Topic: Basic While Loops

**Explanation:**
`while` loops execute a block as long as a condition remains `True`. You can initialize a counter outside the loop and increment it each iteration.

**Example:**

```python
n = int(input("Enter a number: "))
i = 0
while i < n:
    print(i)
    i += 1
```

**Questions I have done on that topic:**

* Question 2: Printed all integers from 0 up to (but not including) the user’s input `n`.

---

### Topic: Conditional Statements (if–elif–else)

**Explanation:**
Use `if`, `elif`, and `else` to branch logic based on multiple mutually exclusive conditions.

**Example:**

```python
n = int(input("Enter a number: "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("0")
```

**Questions I have done on that topic:**

* Question 3: Classified the user’s integer as positive, negative, or zero.

---

### Topic: Finding the Largest of Three Numbers

**Explanation:**
Read three values, convert to integers, then use logical comparisons (`and`) in chained `if–elif–else` to determine which is greatest.

**Example:**

```python
a, b, c = input("Enter three numbers: ").split(", ")
a, b, c = int(a), int(b), int(c)
if a > b and a > c:
    print(f"{a} is the largest")
elif b > a and b > c:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")
```

**Questions I have done on that topic:**

* Question 4: Compared three inputs and printed the largest value.

---

### Topic: Grade Classification with if–elif Ladder

**Explanation:**
Use a sequence of `elif` checks to classify numeric marks into grade categories (“A” through “Fail”), handling invalid inputs first.

**Example:**

```python
marks = int(input("Enter your marks: "))
if marks > 100:
    print("Please enter valid marks")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("Fail")
```

**Questions I have done on that topic:**

* Question 5: Printed grade (A–D or Fail) based on user’s marks, with validation for marks over 100.

---

### Topic: For Loops & Even Number Check

**Explanation:**
A `for` loop can iterate over a range of integers. Using the modulo operator (`%`), you can test each number for evenness (`i % 2 == 0`) before printing.

**Example:**

```python
n = int(input("Enter a number: "))
for i in range(0, n+1):
    if i % 2 == 0:
        print(i)
```

**Questions I have done on that topic:**

* Question 6: Printed all even numbers from 0 up to the user’s input `n`.

---

### Topic: Summing Digits of a Number

**Explanation:**
Extract each digit by taking the remainder (`n % 10`) and floor-dividing (`n //= 10`) inside a `while` loop, accumulating the sum.

**Example:**

```python
n = int(input("Enter a number: "))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(f"sum: {total}")
```

**Questions I have done on that topic:**

* Question 7: Computed and printed the sum of all digits in the user’s number.

---

### Topic: Loop Control Statements (`continue` & `break`)

**Explanation:**

* `continue` skips the rest of the current iteration and proceeds with the next.
* `break` exits the loop entirely.

**Examples:**

```python
# continue example
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# break example
for i in range(10, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        break
```

**Questions I have done on that topic:**

* Question 8: Used `continue` to skip printing when `i == 5`.
* Question 9: Used `break` to stop at the first number divisible by both 5 and 7 between 10 and 100.

---

### Topic: FizzBuzz Implementation

**Explanation:**
Classic loop exercise: for each integer, print “Fizz” if divisible by 3, “Buzz” if by 5, “FizzBuzz” if by both, and skip others.

**Example:**

```python
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} : FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} : Fizz")
    elif i % 5 == 0:
        print(f"{i} : Buzz")
```

**Questions I have done on that topic:**

* Question 10: Implemented FizzBuzz for numbers 1 through 50.

---

### Topic: Multiplication Table

**Explanation:**
Generate and print the multiplication table of a given number `n` by iterating `i` from 1 to 10 and multiplying.

**Example:**

```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
```

**Questions I have done on that topic:**

* Question 11: Displayed the 1× to 10× multiplication table for user’s `n`.

---

### Topic: Prime Number Checking

**Explanation:**
To test if `n` is prime, rule out divisors from 2 up to `sqrt(n)`. If none divide `n` evenly, it’s prime.

**Example:**

```python
n = int(input("Enter a number: "))
if n <= 1:
    print("not prime")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "not prime")
```

**Questions I have done on that topic:**

* Question 12: Checked and reported whether the input `n` is prime.

---

### Topic: Prime Number Generation up to N

**Explanation:**
List all primes ≤ `n` by testing each candidate `i` using the same sieve-like divisor check up to `sqrt(i)`.

**Example:**

```python
n = int(input("Enter upper limit: "))
for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)
```

**Questions I have done on that topic:**

* Question 13: Printed every prime number between 2 and the user’s limit `n`.

