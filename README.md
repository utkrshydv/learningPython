# **📚 learningPython**

<details>
 <summary>
 🧪 Lab 1
 </summary>

### **💡 Topic:** Basic Input/Output & f-strings

**📝 Explanation:**
Python’s built-in `input()` function reads a line of text from the user as a string. To display output, you can use `print()`. f-strings (`f"…{expr}…"`) let you embed expressions directly inside string literals for readable formatting.

**⭐ Example:**

 ```python
 name = input("Enter your name: ")
 age  = input("Enter your age: ")
 print(f"Hello {name}. You're {age} years old")
 ```

**✅ Questions I have done on that topic:**

* Question 1: Greeted the user by name and age using `input()` and an f-string.

---

### **🔢 Topic:** Type Conversion & Addition

**📝 Explanation:**
User input is always a string. To perform numeric operations, convert with `int()` or `float()`. You can then add mixed types (e.g. `int + float`) and Python will promote to the more general `float`.

**⭐ Example:**

 ```python
 num1  = int(input("Enter a number: "))
 num2  = float(input("Enter a float: "))
 total = num1 + num2
 print(f"The sum is: {total}")
 ```

**✅ Questions I have done on that topic:**

* Question 2: Converted inputs to `int` and `float`, then printed their sum.

---

### **➕➖✖️➗ Topic:** Arithmetic Operators

**📝 Explanation:**
Python supports the usual arithmetic operators:

* `+` (addition)
* `-` (subtraction)
* `*` (multiplication)
* `/` (true division)
* `//` (floor division)
* `%` (modulus)
* `**` (exponentiation)

**⭐ Example:**

 ```python
 a = 10
 b =  3
 print("Addition:         ", a + b)
 print("Subtraction:      ", a - b)
 print("Multiplication: ", a * b)
 print("Division:         ", a / b)
 print("Floor Division: ", a // b)
 print("Modulus:          ", a % b)
 print("Exponentiation: ", a ** b)
 ```

**✅ Questions I have done on that topic:**

* Question 3: Demonstrated all basic arithmetic operators with `a = 10` and `b = 3`.

---

### **✂️ Topic:** String Splitting & Multiple Assignment

**📝 Explanation:**
The string method `.split(sep)` breaks a string into a list by the given separator. You can then unpack those list elements directly into multiple variables in one line.

**⭐ Example:**

 ```python
 name, age, score = input("Enter name, age and score: ").split(", ")
 print(f"name: {name}, age: {age}, score: {score}")
 ```

**✅ Questions I have done on that topic:**

* Question 4: Read three comma-separated values and assigned them to `name`, `age`, and `score`.

---

### **🔗 Topic:** Converting & Concatenating Numeric Strings

**📝 Explanation:**
You can convert string representations of numbers back to numeric types (`int`, `float`), do arithmetic, and then convert back to strings for concatenation.

**⭐ Example:**

 ```python
 int_str   = int(input("Enter integer as string: "))
 float_str = float(input("Enter float as string: "))

 print(int_str, float_str)               # numeric output
 print(int_str + float_str)               # arithmetic sum
 print(str(int_str) + str(float_str))     # string concatenation
 ```

**✅ Questions I have done on that topic:**

* Question 5: Converted inputs from strings to numbers, then demonstrated both arithmetic addition and string concatenation.

---

### **🚦 Topic:** Conditional Statements

**📝 Explanation:**
Use `if`, `else` (and optionally `elif`) to execute code blocks based on boolean conditions.

**⭐ Example:**

 ```python
 marks = float(input("Enter your marks: "))
 if marks >= 40:
     print("Passed")
 else:
     print("Failed")
 ```

**✅ Questions I have done on that topic:**

* Question 6: Checked pass/fail status based on a single `marks` input.

---

### **📊 Topic:** Calculating Percentage & Average

**📝 Explanation:**
You can perform compound arithmetic expressions to compute percentages and averages:

* **Percentage** = `(sum of marks) / (total maximum) * 100`
* **Average** = `(sum of marks) / (number of subjects)`

**⭐ Examples:**

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

**✅ Questions I have done on that topic:**

* Question 7: Calculated percentage from three subject marks.
* Question 8: Computed average of three marks and used a conditional to print pass/fail.

---
</details>

<details>
 <summary>
🎮 Lab 2
</summary>

### **🎲 Topic:** Random Number Guessing Game

**📝 Explanation:**
This program uses the `random` module to generate a secret integer between 1 and 10. A `while True` loop repeatedly prompts the user to guess; based on the comparison, it prints hints ("guess higher"/"guess lower") until the correct number is guessed, then breaks out of the loop.

**⭐ Example:**

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

**✅ Questions I have done on that topic:**

* Question 1: Built a guessing game that loops until the user finds the randomly chosen number, using `continue` and `break`.

---

### **🔄 Topic:** Basic While Loops

**📝 Explanation:**
`while` loops execute a block as long as a condition remains `True`. You can initialize a counter outside the loop and increment it each iteration.

**⭐ Example:**

 ```python
 n = int(input("Enter a number: "))
 i = 0
 while i < n:
     print(i)
     i += 1
 ```

**✅ Questions I have done on that topic:**

* Question 2: Printed all integers from 0 up to (but not including) the user’s input `n`.

---

### **🚦 Topic:** Conditional Statements (if–elif–else)

**📝 Explanation:**
Use `if`, `elif`, and `else` to branch logic based on multiple mutually exclusive conditions.

**⭐ Example:**

 ```python
 n = int(input("Enter a number: "))
 if n > 0:
     print("positive")
 elif n < 0:
     print("negative")
 else:
     print("0")
 ```

**✅ Questions I have done on that topic:**

* Question 3: Classified the user’s integer as positive, negative, or zero.

---

### **🥇 Topic:** Finding the Largest of Three Numbers

**📝 Explanation:**
Read three values, convert to integers, then use logical comparisons (`and`) in chained `if–elif–else` to determine which is greatest.

**⭐ Example:**

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

**✅ Questions I have done on that topic:**

* Question 4: Compared three inputs and printed the largest value.

---

### **🎓 Topic:** Grade Classification with if–elif Ladder

**📝 Explanation:**
Use a sequence of `elif` checks to classify numeric marks into grade categories (“A” through “Fail”), handling invalid inputs first.

**⭐ Example:**

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

**✅ Questions I have done on that topic:**

* Question 5: Printed grade (A–D or Fail) based on user’s marks, with validation for marks over 100.

---

### **➡️ Topic:** For Loops & Even Number Check

**📝 Explanation:**
A `for` loop can iterate over a range of integers. Using the modulo operator (`%`), you can test each number for evenness (`i % 2 == 0`) before printing.

**⭐ Example:**

 ```python
 n = int(input("Enter a number: "))
 for i in range(0, n+1):
     if i % 2 == 0:
         print(i)
 ```

**✅ Questions I have done on that topic:**

* Question 6: Printed all even numbers from 0 up to the user’s input `n`.

---

### **➕ Topic:** Summing Digits of a Number

**📝 Explanation:**
Extract each digit by taking the remainder (`n % 10`) and floor-dividing (`n //= 10`) inside a `while` loop, accumulating the sum.

**⭐ Example:**

 ```python
 n = int(input("Enter a number: "))
 total = 0
 while n > 0:
     total += n % 10
     n //= 10
 print(f"sum: {total}")
 ```

**✅ Questions I have done on that topic:**

* Question 7: Computed and printed the sum of all digits in the user’s number.

---

### **⏯️ Topic:** Loop Control Statements (`continue` & `break`)

**📝 Explanation:**

* `continue` skips the rest of the current iteration and proceeds with the next.
* `break` exits the loop entirely.

**⭐ Examples:**

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

**✅ Questions I have done on that topic:**

* Question 8: Used `continue` to skip printing when `i == 5`.
* Question 9: Used `break` to stop at the first number divisible by both 5 and 7 between 10 and 100.

---

### **🧩 Topic:** FizzBuzz Implementation

**📝 Explanation:**
Classic loop exercise: for each integer, print “Fizz” if divisible by 3, “Buzz” if by 5, “FizzBuzz” if by both, and skip others.

**⭐ Example:**

 ```python
 for i in range(1, 51):
     if i % 3 == 0 and i % 5 == 0:
         print(f"{i} : FizzBuzz")
     elif i % 3 == 0:
         print(f"{i} : Fizz")
     elif i % 5 == 0:
         print(f"{i} : Buzz")
 ```

**✅ Questions I have done on that topic:**

* Question 10: Implemented FizzBuzz for numbers 1 through 50.

---

### **✖️ Topic:** Multiplication Table

**📝 Explanation:**
Generate and print the multiplication table of a given number `n` by iterating `i` from 1 to 10 and multiplying.

**⭐ Example:**

 ```python
 n = int(input("Enter a number: "))
 for i in range(1, 11):
     print(f"{n} x {i} = {n*i}")
 ```

**✅ Questions I have done on that topic:**

* Question 11: Displayed the 1× to 10× multiplication table for user’s `n`.

---

### **⭐ Topic:** Prime Number Checking

**📝 Explanation:**
To test if `n` is prime, rule out divisors from 2 up to `sqrt(n)`. If none divide `n` evenly, it’s prime.

**⭐ Example:**

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

**✅ Questions I have done on that topic:**

* Question 12: Checked and reported whether the input `n` is prime.

---

### **✨ Topic:** Prime Number Generation up to N

**📝 Explanation:**
List all primes ≤ `n` by testing each candidate `i` using the same sieve-like divisor check up to `sqrt(i)`.

**⭐ Example:**

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

**✅ Questions I have done on that topic:**

* Question 13: Printed every prime number between 2 and the user’s limit `n`.

</details>
<details>
 <summary>
🛠️ Lab 3
</summary>

### **⚙️ Topic:** Function Definition & Return Values

**📝 Explanation:**
Functions in Python are defined using the `def` keyword, followed by a name, parameters in parentheses, and a colon. Inside the function, use `return` to send a value back to the caller. If no `return` is given, the function returns `None`.

**⭐ Example:**

 ```python
 def add_numbers(a, b):
     return a + b

 x, y = input("Enter two numbers: ").split(", ")
 print("Sum: ", add_numbers(int(x), int(y)))
 ```

**✅ Questions I have done on that topic:**

* Question 1: Defined `add_numbers(a, b)` to return the sum of two integers read from input.

---

### **🚦 Topic:** Conditional Logic in Functions

**📝 Explanation:**
Functions can contain conditional statements to execute different logic paths. A simple `if–else` inside a function can return different results based on input.

**⭐ Example:**

 ```python
 def even_odd(num):
     if num % 2 == 0:
         return "even"
     else:
         return "odd"

 n = int(input("Enter a number: "))
 print("The number is", even_odd(n))
 ```

**✅ Questions I have done on that topic:**

* Question 2: Wrote `even_odd(num)` to classify an integer as "even" or "odd".

---

### **🔄️ Topic:** Recursive Functions

**📝 Explanation:**
A recursive function calls itself with a modified argument until a base case is met. Careful base-case definition prevents infinite recursion.

**⭐ Example:**

 ```python
 def find_factorial(num):
     if num == 1:
         return 1
     return num * find_factorial(num - 1)

 n = int(input("Enter number: "))
 print(f"The factorial is: {find_factorial(n)}")
 ```

**✅ Questions I have done on that topic:**

* Question 3: Implemented `find_factorial(num)` recursively to compute the factorial of `n`.

---

### **🏆 Topic:** Finding the Maximum of Three Values

**📝 Explanation:**
Use a combination of `if–elif–else` and logical comparisons (`>`) to compare three values and return the largest.

**⭐ Example:**

 ```python
 def find_max(a, b, c):
     if a > b and a > c:
         return a
     elif b > a and b > c:
         return b
     else:
         return c

 print(f"Largest number is: {find_max(5, 6, 7)}")
 ```

**✅ Questions I have done on that topic:**

* Question 4: Created `find_max(a, b, c)` to return the largest of three hard-coded values.

---

### **📦 Topic:** Built-in List Functions (`len`, `sum`, `type`)

**📝 Explanation:**
Python provides built-in functions for common list operations:

* `len(list)` returns the number of elements.
* `sum(list)` returns the sum of numeric elements.
* `type(value)` returns the data type of `value`.

**⭐ Example:**

 ```python
 my_list = [10, 20, 30]
 print("Length: ", len(my_list))
 print("Sum: ", sum(my_list))
 print("Type of sum: ", type(sum(my_list)))
 ```

**✅ Questions I have done on that topic:**

* Question 5: Demonstrated use of `len()`, `sum()`, and `type()` on a sample list.

---

### **➕ Topic:** Calculating Average of a List

**📝 Explanation:**
Compute the average by dividing the sum of elements by the length of the list. You can write a reusable function that takes a list argument.

**⭐ Example 1:**

 ```python
 def find_average(numbers):
     return sum(numbers) / len(numbers)

 nums = [10, 20, 30, 40]
 print("Average: ", find_average(nums))
 ```

**⭐ Example 2 (with `map`):**

 ```python
 def find_avg(number):
     return sum(number) / len(number)

 num = list(map(int, input("Enter numbers separated by space: ").split(" ")))
 print(f"Average: {find_avg(num)}")
 ```

**✅ Questions I have done on that topic:**

* Question 6: Wrote `find_average(numbers)` to compute average of a hard-coded list.
* Question 7: Used `map(int, …)` to parse user input into a list of integers, then computed average.

---

### **🔍 Topic:** Finding Maximum in a List (Custom vs. Built-in)

**📝 Explanation:**
You can manually iterate through a list to find the maximum value, or simply call Python’s built-in `max()` function.

**⭐ Example:**

 ```python
 def find_max_in_list(number):
     max_val = number [0]
     for num in number:
         if num > max_val:
             max_val = num
     return max_val

 def find_max_prebuilt(numbers):
     return max(numbers)

 n = list(map(int, input("Enter numbers separated by space: ").split(" ")))
 print(f"max: {find_max_in_list(n)}")
 print(f"max: {find_max_prebuilt(n)}")
 ```

**✅ Questions I have done on that topic:**

* Question 8: Implemented `find_max_in_list(number)` manually.
* Question 9: Used built-in `max(numbers)` for comparison.

---

### **🔢 Topic:** Counting Even Numbers in a List

**📝 Explanation:**
Iterate through a list, test each element for evenness (`% 2 == 0`), and maintain a counter that you return at the end.

**⭐ Example:**

 ```python
 def count_even(number):
     count = 0
     for num in number:
         if num % 2 == 0:
             count += 1
     return count

 num = list(map(int, input("Enter numbers: ").split(" ")))
 print(f"even : {count_even(num)}")
 ```

**✅ Questions I have done on that topic:**

* Question 10: Wrote `count_even(number)` to count and return the number of even integers in the user-provided list.

---

### **🔪 Topic: List Slicing in Python**

**📝 Explanation:**

List slicing allows you to extract specific portions of a list using the syntax:

 ```python
 list [start:stop:step]
 ```

* **start**: Index where the slice begins (inclusive).
* **stop**: Index where the slice ends (exclusive).
* **step**: (Optional) Interval between elements (default is 1).

Negative indices count from the end of the list.

---

###  **🧪 Examples and Challenges**

---

####  **✂️ Basic Slicing Examples**

 ```python
 my_list = [10, 20, 30, 40, 50, 60]
 ```

 ```python
 # First 4 items
 print(my_list[:4])  # [10, 20, 30, 40]

 # All except first and last
 print(my_list [1:-1])  # [20, 30, 40, 50]

 # Reverse first 3 items
 print(my_list [:3][::-1])  # [30, 20, 10]

 # Last 3 items in reverse
 print(my_list [:-4-1:-1])  # [60, 50, 40]

 # Every 2nd item from index 1
 print(my_list [1::2])  # [20, 40, 60]

 # Copy entire list
 print(my_list [:])  # [10, 20, 30, 40, 50, 60]
 ```

---

####  **💪 Practice Challenges**

1. **Middle section excluding first and last**

 ```python
 lst = [5, 10, 15, 20, 25, 30]
 print(lst [1:-1])  # [10, 15, 20, 25]
 ```

2. **Reverse only first 4 elements**

 ```python
 lst = [1, 2, 3, 4, 5, 6]
 print(lst [:4][::-1] + lst [4:])  # [4, 3, 2, 1, 5, 6]
 ```

3. **Last 4 elements reversed**

 ```python
 lst = [11, 22, 33, 44, 55, 66, 77]
 print(lst [-1:-5:-1])  # [77, 66, 55, 44]
 ```

4. **Every 3rd element starting from index 1**

 ```python
 lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 print(lst [1::3])  # [1, 4, 7]
 ```

5. **Copy list without last 2 elements**

 ```python
 lst = [100, 200, 300, 400, 500]
 print(lst [:-2])  # [100, 200, 300]
 ```

---

###  **🧠 Advanced Revision Challenges**

1. **First 5 elements reversed**

 ```python
 lst = [10, 20, 30, 40, 50, 60, 70]
 print(lst [:5][::-1])  # [50, 40, 30, 20, 10]
 ```

2. **From index 3 to 6**

 ```python
 lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
 print(lst [3:7])  # [3, 4, 5, 6]
 ```

3. **Last 5 elements**

 ```python
 lst = [5, 10, 15, 20, 25, 30, 35, 40]
 print(lst [-5:])  # [20, 25, 30, 35, 40]
 ```

4. **Every 3rd from index 2**

 ```python
 lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
 print(lst [2::3])  # [3, 6, 9]
 ```

---

###  **🎯 Final Slicing Challenge**

 ```python
 lst = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
 ```

1. **Last 3 elements in reverse**

 ```python
 print(lst [-1:-4:-1])  # [50, 45, 40]
 ```

2. **Skip every other element**

 ```python
 print(lst [::2])  # [5, 15, 25, 35, 45]
 ```

3. **Index 2 to 7 in reverse**

 ```python
 print(lst [2:8][::-1])  # [40, 35, 30, 25, 20, 15]
 ```

4. **Exclude first 2 and last 2**

 ```python
 print(lst [2:-2])  # [15, 20, 25, 30, 35, 40]
 ```

5. **Reverse list and take every 3rd item**

 ```python
 print(lst [::-1][::3])  # [50, 35, 20, 5]
 ```

---


### **🛠️ Topic:** List Methods (`append`, `insert`, `remove`, `sort`, `reverse`)

**📝 Explanation:**
Python lists provide built-in methods to modify their contents in place:

* `append(item)` adds `item` to the end.
* `insert(index, item)` places `item` at position `index`.
* `remove(item)` deletes the first occurrence of `item`.
* `sort()` arranges elements in ascending order.
* `reverse()` reverses the list in place.

**⭐ Example:**

 ```python
 lst = [1, 3, 5]
 lst.append(7)        # [1, 3, 5, 7]
 lst.insert(1, 2)     # [1, 2, 3, 5, 7]
 lst.remove(3)        # [1, 2, 5, 7]
 lst.sort()           # [1, 2, 5, 7]
 lst.reverse()        # [7, 5, 2, 1]
 print(lst)           # [7, 5, 2, 1]
 ```

**✅ Questions I have done on that topic:**

* Question 1: Used `append()` to add a single element at the end of a list.
* Question 2: Used `insert()` to place a new element at a specific index.
* Question 3: Used `remove()` to delete a given element by value.
* Question 4: Used `sort()` to sort a list of numbers in ascending order.
* Question 5: Used `reverse()` to reverse the order of a list.

---

### **🔢 Topic:** Counting & Finding Elements (`count`, `index`)

**📝 Explanation:**

* `count(item)` returns how many times `item` appears in the list.
* `index(item)` returns the first index at which `item` appears (raises an error if not found).

**⭐ Example:**

 ```python
 fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
 print(fruits.count('apple'))    # 3

 colors = ['red', 'blue', 'green', 'blue', 'yellow']
 print(colors.index('blue'))     # 1
 ```

**✅ Questions I have done on that topic:**

* Question 1: Counted occurrences of `'apple'` in a list of fruit names.
* Question 2: Found the index of the first `'blue'` in a list of colors.

---

### **📑 Topic:** Copying Lists (shallow vs. deep)

**📝 Explanation:**

* `list.copy()` creates a shallow copy: a new list object, but nested objects remain shared.
* `copy.deepcopy()` (from the `copy` module) creates a full deep copy: all levels duplicated.

**⭐ Example:**

 ```python
 import copy

 # Shallow copy of flat list
 numbers = [5, 10, 15]
 copy_numbers = numbers.copy()
 copy_numbers.append(44)
 # numbers remains [5, 10, 15], copy_numbers is [5, 10, 15, 44]

 # Deep copy of nested list
 original = [[1, 2], [3, 4]]
 deep_copy = copy.deepcopy(original)
 deep_copy [0].append(99)
 # original stays [[1, 2], [3, 4]]
 # deep_copy is [[1, 2, 99], [3, 4]]
 ```

**✅ Questions I have done on that topic:**

* Question 1: Created a shallow copy of a simple list and showed modifications don’t affect the original.
* Question 2: Created a deep copy of a nested list and demonstrated independence from the original.

---

### **✂️➕ Topic:** Removing & Extending Lists (`pop`, `extend`)

**📝 Explanation:**

* `pop()` removes and returns the last element (or at a given index if provided).
* `extend(iterable)` appends all elements from `iterable` to the end of the list.

**⭐ Example:**

 ```python
 lst = [10, 20, 30, 40]
 x = lst.pop()           # x = 40, lst = [10, 20, 30]
 lst.extend([20, 25])     # lst = [10, 20, 30, 20, 25]
 print(x, lst)
 ```

**✅ Questions I have done on that topic:**

* Question 1: Used `pop()` to remove and capture the last element of a list.
* Question 2: Used `extend()` to add multiple new items onto a list.

---

### **⚡ Topic:** Functional Tools (`map` & `filter` with `lambda`)

**📝 Explanation:**

* `map(func, iterable)` applies `func` to every item and returns an iterator of results.
* `filter(func, iterable)` returns an iterator of items for which `func(item)` is `True`.
* Combine `filter()` and `map()` to first select items, then transform them.

**⭐ Example:**

 ```python
 nums = [2, 3, 4]
 squares    = list(map(lambda x: x*x, nums))
 evens      = list(filter(lambda x: x % 2 == 0, nums))
 square_evens = list(map(lambda x: x*x, filter(lambda x: x%2 == 0, nums)))
 print(squares)     # [4, 9, 16]
 print(evens)       # [2, 4]
 print(square_evens) # [4, 16]
 ```

**✅ Questions I have done on that topic:**

* Question 1: Used `map()` with a `lambda` to compute squares of a list of numbers.
* Question 2: Used `filter()` with a `lambda` to extract even numbers.
* Question 3: Combined `filter()` and `map()` to square only the even numbers.

---

### **✨ Topic:** List Comprehensions

**📝 Explanation:**
List comprehensions provide a concise syntax to build lists:

 ```python
 [expression for item in iterable if condition]
 ```

They can include an `if…else` inside the expression for conditional output.

**⭐ Example:**

 ```python
 # Squares of 1–10
 squared_nums   = [i*i for i in range(1, 11)]

 # Words starting with 'a'
 words            = ['apple', 'banana', 'avocado', 'berry', 'apricot']
 starts_with_a    = [w for w in words if w [0] == 'a']

 # Even numbers doubled
 nums             = [1, 2, 3, 4, 5, 6]
 multiplied_by_2 = [x*2 for x in nums if x % 2 == 0]

 # Label odd/even
 nums             = [7, 2, 5, 8]
 odd_even       = ["even" if x % 2 == 0 else "odd" for x in nums]
 ```

**✅ Questions I have done on that topic:**

* Question 1: Generated a list of squares using a comprehension.
* Question 2: Filtered a list of strings to those starting with `'a'`.
* Question 3: Created a list of doubled values only for even numbers.
* Question 4: Used a conditional expression inside a comprehension to label each number `"even"` or `"odd"`.
</details>
