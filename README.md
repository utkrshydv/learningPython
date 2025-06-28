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

<details>

<summary>✅ Lab 4</summary> 

### 🧵 Topic: **Tuples**

**Explanation:**
A **tuple** is an ordered, immutable collection of elements. This means once a tuple is created, you cannot change, add, or remove elements from it. Tuples are used to group related data together and ensure that the grouped data stays constant.

They're defined using parentheses `()` and support indexing, slicing, nesting, and unpacking.

**Example:**

```python
my_tuple = (1, 2, 3, 4)
print(my_tuple[1])  # Output: 2

person = ('utkarsh', 21, 'Engineer', 'male')
name, age, job, gender = person
print(name, age, job, gender)
```

---

### 🧵 Topic: **Tuple Unpacking**

**Explanation:**
Tuple unpacking allows you to assign each item in a tuple to a variable in a single line. The number of variables must match the number of elements in the tuple.

**Example:**

```python
t2 = ('python', 3.10, True)
lang, version, is_dynamic = t2
print(lang)  # python
```

---

### 🧵 Topic: **Singleton Tuple**

**Explanation:**
To create a tuple with only one element, you must include a trailing comma. Otherwise, Python treats it as a regular value.

**Example:**

```python
t3 = (42,)  # This is a tuple
print(type(t3))  # <class 'tuple'>

not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>
```

---

### 🧵 Topic: **Tuple Slicing**

**Explanation:**
Just like strings and lists, tuples can be sliced to retrieve a portion of elements using the syntax `tuple[start:stop:step]`.

**Example:**

```python
t = (10, 20, 30, 40, 50)
print(t[1:4])     # (20, 30, 40)
print(t[::-1])    # Reverses the tuple
```

---

### 🧵 Topic: **Tuple Methods: `count()` and `index()`**

**Explanation:**

* `count(x)` → returns the number of times `x` appears in the tuple.
* `index(x)` → returns the index of the first occurrence of `x`.

**Example:**

```python
t = (3, 6, 3, 9, 3, 12)
print(t.count(3))  # 3
print(t.index(9))  # 3
```

---

### 🧵 Topic: **Nested Tuples**

**Explanation:**
Tuples can contain other tuples or complex data types. Access elements using multiple indices.

**Example:**

```python
person = ("utkarsh", (21, 'M'), ("python", "java"))
print(person[1][0])  # 21
print(person[2][1])  # java
```

---

### 🧵 Topic: **Sets**

**Explanation:**
A set is an unordered collection of **unique** elements. Sets are used when you want to store distinct values and perform operations like union, intersection, difference, etc.

**Example:**

```python
nums = {1, 2, 3, 3, 4}
print(nums)  # {1, 2, 3, 4} – duplicates removed
```

---

### 🧵 Topic: **Set Operations**

**Explanation:**

* `|` → Union
* `&` → Intersection
* `-` → Difference
* `^` → Symmetric Difference

**Example:**

```python
a = {1, 2, 3}
b = {2, 3, 6}

print(a | b)  # {1, 2, 3, 6}
print(a & b)  # {2, 3}
print(a - b)  # {1}
print(a ^ b)  # {1, 6}
```

---

### 🧵 Topic: **Set from String**

**Explanation:**
Converting a string to a set helps in extracting unique characters.

**Example:**

```python
word = "balloon"
unique_letters = set(word)
print(unique_letters)  # {'b', 'a', 'l', 'o', 'n'}
```

---

### 🧵 Topic: **Dictionaries**

**Explanation:**
Dictionaries store data as key-value pairs. Keys are unique, and values can be of any data type. Useful for fast lookups and organizing data meaningfully.

**Example:**

```python
student = {
    'name': 'utkarsh',
    'age': 21,
    'courses': ['Math', 'Science']
}
print(student['name'])  # utkarsh
```

---

### 🧵 Topic: **Dictionary Methods: `get()`, `pop()`, `del`**

**Explanation:**

* `get(key)` → returns the value or `None` if the key doesn't exist.
* `pop(key)` → removes and returns the value of the given key.
* `del` → deletes a key-value pair from the dictionary.

**Example:**

```python
student.get('email')             # None
student.pop('grade')             # removes 'grade'
del student['age']               # removes 'age'
```

---

### 🧵 Topic: **Looping Through a Dictionary**

**Explanation:**
You can iterate over keys, values, or both using `keys()`, `values()`, or `items()`.

**Example:**

```python
for key, value in student.items():
    print(f"{key} : {value}")
```

---

### 🧵 Topic: **Nested Dictionaries**

**Explanation:**
A dictionary can store another dictionary as a value. Useful for structured, grouped data.

**Example:**

```python
classroom = {
    'utkarsh': {'age': 21, 'grade': 90},
    'disha': {'age': 32, 'grade': 100}
}
print(classroom['disha']['grade'])  # 100
```

---

### 🧵 Topic: **Real-world Dictionary Use Cases**

#### 📞 Phonebook Lookup

**Explanation:**
Get a value from a dictionary safely using `get()` to avoid errors if the key is missing.

**Example:**

```python
name = input("Enter a name: ")
print(phonebook.get(name, "Not found"))
```

#### 🍎 Inventory Update

**Explanation:**
Simulates real-time item stock updates.

**Example:**

```python
inventory['banana'] -= 2
inventory['grapes'] = 15
```

#### 🔁 Word Frequency Counter

**Explanation:**
Counts how many times each word appears in a sentence.

**Example:**

```python
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
```
</details>




<details>
<summary>🧪 Lab 5</summary>  

 
### **Topic: Object-Oriented Programming (OOP) in Python**


### 🧵 Topic: **Classes and Objects**

**Explanation:**  
A **class** is a blueprint for creating objects. It defines attributes (variables) and methods (functions) that its instances (objects) will have. Objects are instances of a class and represent real-world entities.

**Example:**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old")

s1 = Student("utkarsh", 21)
s1.introduce()
````

---

### 🧵 Topic: **Constructors (`__init__`)**

**Explanation:**
The `__init__` method is automatically called when a new object is created. It initializes the object’s attributes.

**Example:**

```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
```

---

### 🧵 Topic: **Instance Methods**

**Explanation:**
Instance methods operate on the data stored in an object. They’re defined inside a class and use `self` to access instance variables.

**Example:**

```python
class Account:
    def display(self):
        print(f"owner: {self.owner}, balance: {self.balance}")
```

---

### 🧵 Topic: **Default Parameter Values**

**Explanation:**
Default values in constructors let you make parameters optional when creating objects.

**Example:**

```python
class Person:
    def __init__(self, name, city="unknown"):
        self.name = name
        self.city = city
```

---

### 🧵 Topic: **Conditional Logic in Methods**

**Explanation:**
Methods can include logic such as validations or branching. For example, checking if balance is sufficient before withdrawing.

**Example:**

```python
def withdraw(self, amount):
    if amount > self.balance:
        print("insufficient balance")
    else:
        self.balance -= amount
```

---

### 🧵 Topic: **Working with Lists Inside Classes**

**Explanation:**
Objects can have attributes that are lists to store multiple items, such as grades or products.

**Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grade = []

    def add_grade(self, grade):
        self.grade.append(grade)

    def average(self):
        return sum(self.grade)/len(self.grade)
```

---

### 🧵 Topic: **Composition: Object Inside Object**

**Explanation:**
Composition is when a class contains instances of other classes. Useful for building real-world relationships like Library → Book.

**Example:**

```python
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
```

---

### 🧵 Topic: **Encapsulation**

**Explanation:**
Encapsulation groups data and methods that operate on that data into one unit — the class. It helps keep the internal details hidden and only exposes necessary functionality.

---

### 🧵 Topic: **Inheritance**

**Explanation:**
Inheritance lets one class (child) inherit the properties and methods of another class (parent). It enables code reuse and establishes a hierarchy.

**Example:**

```python
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof")
```

---

### 🧵 Topic: **`super()` Keyword**

**Explanation:**
`super()` allows access to methods and properties of a parent class from within a child class. Often used to call the parent’s `__init__` method.

**Example:**

```python
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
```

---

### 🧵 Topic: **Polymorphism via Method Overriding**

**Explanation:**
Polymorphism allows different classes to define methods with the same name but different behavior. Method overriding customizes inherited methods.

**Example:**

```python
class Rectangle(Shape):
    def area(self):
        return self.length * self.breadth
```

---

### 🧵 Topic: **Class vs Instance Variables**

**Explanation:**

* **Instance variables** (like `self.name`) are unique to each object.
* **Class variables** (like `species`) are shared across all instances of the class.

**Example:**

```python
class Dog:
    species = "Canis Familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name           # Instance variable
```

---

### 🧵 Topic: **Class Methods**

**Explanation:**
Class methods use the `@classmethod` decorator and receive the class as the first argument (`cls`). They're used to access or modify class-level data.

**Example:**

```python
class Counter:
    counter = 0

    @classmethod
    def get_total(cls):
        print(cls.counter)
```

---

### 🧵 Topic: **Practical OOP Examples**

**Explanation:**
These examples implement real-life use cases using OOP concepts like classes, composition, and inheritance.

**Example:**

```python
# Library and Book
lib.add_book(Book("1984", "George Orwell"))
lib.borrow_book("1984")

# Cart and Product
cart.add_product(Product("T-shirt", 20.0))
print(cart.total_price())

# Movie and MovieCollection
collection.find_by_director("Christopher Nolan")

# Playlist and Song
my_playlist.play_all()
my_playlist.remove_song("Bohemian Rhapsody")

# SavingsAccount (extends Account)
a1 = SavingsAccount("utkarsh", 1000, 7)
a1.apply_interest()
```

### 🧵 Topic: **Multiple Inheritance**

**Explanation:**  
Multiple inheritance allows a class to inherit from more than one parent class. Python resolves method calls using **Method Resolution Order (MRO)** — left to right in the class declaration.

**Example:**
```python
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()   # Output: Hello from A
print(C.mro())
````

---

### 🧵 Topic: **Abstract Classes & Interfaces (ABC module)**

**Explanation:**
Abstract classes are base classes that **cannot be instantiated** and must be inherited.
They contain **abstract methods** (methods with no implementation) using the `@abstractmethod` decorator.

**Example:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of circle")

# shape = Shape()  ❌ Error
```

---

### 🧵 Topic: **Interface-Like Behavior**

**Explanation:**
When a class only defines abstract methods, it behaves like an interface — forcing derived classes to implement all declared behaviors.

**Example:**

```python
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self): pass

class Car(Vehicle):
    def start_engine(self):
        print("car starts")
```

---

### 🧵 Topic: **Encapsulation**

**Explanation:**
Encapsulation means **restricting access** to internal variables and methods.

* `_var` → **protected** (convention)
* `__var` → **private** (name mangled)

**Example:**

```python
class Person:
    def __init__(self):
        self.name = "alex"       # public
        self._hobby = "reading"  # protected
        self.__salary = 50000    # private

    def get_salary(self):
        return self.__salary
```

---

### 🧵 Topic: **Polymorphism**

**Explanation:**
Polymorphism allows different classes to implement the same method in different ways. It works via:

* Method overriding
* Common interface usage (e.g., iterating over different objects with the same method name)

**Example:**

```python
class Dog:
    def make_sound(self):
        print("woof")

class Cat:
    def make_sound(self):
        print("meow")

for animal in [Dog(), Cat()]:
    animal.make_sound()
```

---

### 🧵 Topic: **Real-life Polymorphic Examples**

**Explanation:**
Polymorphism is especially useful when using abstract base classes or unified method calls for different child classes.

**Example:**

```python
class Employee:
    def work(self):
        print("employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is coding")

class Designer(Employee):
    def work(self):
        print("Designer is sketching")

for emp in [Employee(), Developer(), Designer()]:
    emp.work()
```

---

### 🧵 Topic: **OOP Mini Project with Abstract Base Class**

**Explanation:**
Using `ABC` and `@abstractmethod`, you can create a structured system where each class must define required behavior, like a login system or user management.

**Example:**

```python
class User(ABC):
    @abstractmethod
    def login(self): pass

class Student(User):
    def login(self):
        print("Student logged in")
```

---

### 🧵 Topic: **Class Variables & `@classmethod`**

**Explanation:**

* **Class variables** are shared across all instances.
* `@classmethod` is used to access or modify class-level variables or behavior.

**Example:**

```python
class Employee(ABC):
    employee_count = 0

    @classmethod
    def display_count(cls):
        print(cls.employee_count)

class Developer(Employee):
    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1
```

---

### 🧵 Topic: **Summary of OOP Concepts Used**

| Concept                   | Used In                                                |
| ------------------------- | ------------------------------------------------------ |
| Classes & Objects         | `Student`, `Book`, `Account`, etc.                     |
| Inheritance               | `Dog(Animal)`, `Car(Vehicle)`, etc.                    |
| Method Overriding         | `Car.show_info()`, `Developer.work()`                  |
| Encapsulation             | Private/protected attributes like `__salary`, `_marks` |
| Polymorphism              | Loops calling `.work()` on various classes             |
| Abstract Classes          | `Shape`, `MediaFile`, `Employee`                       |
| Multiple Inheritance      | `Robot(Speaker, Mover)`                                |
| Composition               | `Library` contains multiple `Book`                     |
| Class Methods & Variables | `Employee.display_count()`, `Book.total_revenue`       |



---


</details>

<details>
<summary> 🪄Lab 6</summary>

### 🧵 Topic: Dunder (Magic) Methods in Python

**Explanation:**
Dunder methods (short for "double underscore") are special methods in Python that let you override or extend default behavior for built-in operations like printing, comparing, indexing, adding, calling, etc. These methods start and end with double underscores (e.g., `__init__`, `__str__`, `__add__`).

| Dunder Method  | Purpose                                       |
| -------------- | --------------------------------------------- |
| `__init__`     | Constructor, initializes object properties    |
| `__str__`      | Defines output for `print(obj)` or `str(obj)` |
| `__repr__`     | Official representation for debugging         |
| `__eq__`       | Custom logic for equality `==`                |
| `__add__`      | Defines behavior for `+` operator             |
| `__len__`      | Defines behavior for `len(obj)`               |
| `__lt__`       | Defines behavior for `<` operator             |
| `__getitem__`  | Enables indexing like `obj[i]`                |
| `__setitem__`  | Allows assignment like `obj[i] = x`           |
| `__contains__` | Used by `in` keyword                          |
| `__call__`     | Allows objects to be called like functions    |

---

### 📘 `__str__` - String Representation for Users

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'

b1 = Book("1984", "George Orwell")
print(b1)
```

**Explanation:**
`__str__` returns a user-friendly string when the object is printed.

**Output:**

```
"1984" by George Orwell
```

---

### ➕ `__add__` - Overloading `+` Operator

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)
```

**Explanation:**
`__add__` defines how `+` works for two objects. Returns a new Point.

**Output:**

```
Point(6, 8)
```

---

### 🤝 `__eq__` - Overloading `==` Operator

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

p1 = Person("Alice")
p2 = Person("alice")
print(p1 == p2)
```

**Explanation:**
`__eq__` defines how equality is checked. Here, case-insensitive name match.

**Output:**

```
True
```

---

### 💸 `__add__` - Wallets Sum Up

```python
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

    def __str__(self):
        return f'{self.amount}'

w1 = Wallet(50)
w2 = Wallet(100)
w3 = w1 + w2
print(w3)
```

**Explanation:**
Adds the amounts in two wallets and returns a new Wallet.

**Output:**

```
150
```

---

### 📦 `__lt__` - Less Than Comparison

```python
class Box:
    def __init__(self, x, y, z):
        self.volume = x * y * z

    def __lt__(self, other):
        return self.volume < other.volume

b1 = Box(3, 3, 3)
b2 = Box(2, 3, 4)
print(b1 < b2)
print(b2 < b1)
```

**Explanation:**
`__lt__` defines `<` behavior. Compares volumes of the boxes.

**Output:**

```
False
True
```

---

### 📓 `__getitem__` - Indexing Support

```python
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title):
        self.notes.append(title)

    def __getitem__(self, index):
        return self.notes[index]

n = Notebook()
n.add_note("Buy milk")
n.add_note("Study OOP")
print(n[0])
```

**Explanation:**
Allows indexing into custom object like a list.

**Output:**

```
Buy milk
```

---

### 🎒 `__contains__` - `in` Operator

```python
class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __contains__(self, item):
        return item in self.items

inv = Inventory()
inv.add("sword")
print("sword" in inv)
```

**Explanation:**
Enables `in` operator for the custom class.

**Output:**

```
True
```

---

### 🧾 `__setitem__` + `__getitem__` - Dict-like Behavior

```python
class Scoreboard:
    def __init__(self):
        self.scores = {}

    def __setitem__(self, player, score):
        self.scores[player] = score

    def __getitem__(self, player):
        return self.scores[player]

sb = Scoreboard()
sb["Alice"] = 100
print(sb["Alice"])
```

**Explanation:**
Allows dictionary-style assignment and access.

**Output:**

```
100
```

---

### 📞 `__call__` - Make Object Callable

```python
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        print(f"{self.greeting}, {name}!")

j = Greeter("Hello")
j("Utkarsh")
```

**Explanation:**
Allows object to be used like a function call.

**Output:**

```
Hello, Utkarsh!
```

---

### 📋 Full Feature Example: Task Manager

```python
class TaskManager:
    def __init__(self):
        self.tasks = {}

    def __setitem__(self, name, description):
        self.tasks[name] = description

    def __getitem__(self, name):
        return self.tasks[name]

    def __contains__(self, name):
        return name in self.tasks

    def __len__(self):
        return len(self.tasks)

    def __str__(self):
        return f"task manager : {self.tasks}"

    def __repr__(self):
        return f"task manager : {self.tasks}"

    def __call__(self):
        for key in self.tasks:
            print(f"{key} : {self.tasks[key]}")

tm = TaskManager()
tm["laundry"] = "Wash clothes"
tm["study"] = "Python OOP"
print("laundry" in tm)
print(tm["study"])
print(len(tm))
tm()
print(tm)
```

**Explanation:**
Implements multiple dunder methods to make object behave like a dictionary, function, iterable, etc.

**Output:**

```
True
Python OOP
2
laundry : Wash clothes
study : Python OOP
task manager : {'laundry': 'Wash clothes', 'study': 'Python OOP'}
```

---

Each dunder method customizes specific behavior and interaction of objects with Python syntax and built-in operations. Understanding and using them allows you to design more intuitive and powerful custom classes.
</details>

<details>

 <summary> 📂 Lab 7</summary>

### 🗂️ Topic: File Handling in Python

**Explanation:**
File handling in Python lets you work with external files — reading from them, writing to them, appending new data, creating or even deleting files. Python makes this very flexible and simple using built-in functions like `open()` and the `with` statement.

| Mode  | Meaning                               |
| ----- | ------------------------------------- |
| `"r"` | Read (default mode)                   |
| `"w"` | Write (creates or overwrites file)    |
| `"a"` | Append (creates file if not exists)   |
| `"x"` | Create (fails if file already exists) |
| `"b"` | Binary mode (like for images)         |
| `"t"` | Text mode (default)                   |

---

### 📖 Reading from a File

```python
f = open("names.txt", "r")
print(f.read())
f.close()
```

**Explanation:**

* Opens `names.txt` in read mode.
* `.read()` returns the full content.
* `.close()` is used to free the file resource.

---

### 📄 Reading Line by Line

```python
f = open("names.txt", "r")
print(f.readline())  # reads only the first line
f.close()
```

**Explanation:**

* `.readline()` reads one line at a time.
* Useful for large files.

---

### 🔄 Reading File Using Loop

```python
with open("names.txt") as f:
    for line in f:
        print(line.strip())
```

**Explanation:**

* `with` automatically closes the file.
* `.strip()` removes trailing newline.

---

### ✏️ Appending to a File

```python
with open("names.txt", "a") as f:
    f.write("utkarsh6\n")
```

**Explanation:**

* Appends to the end of the file.
* If file doesn’t exist, it is created.

---

### 🧹 Overwriting File (Write Mode)

```python
with open("names.txt", "w") as f:
    f.write("deleted everything")
```

**Explanation:**

* `"w"` overwrites the file from scratch.

---

### 🆕 Creating a New File Safely

```python
import os
if not os.path.exists("utk.txt"):
    with open("utk.txt", "x") as f:
        pass
else:
    print("already exists")
```

**Explanation:**

* `"x"` creates a file only if it doesn’t exist.

---

### ❌ Deleting a File

```python
import os
if os.path.exists("utk.txt"):
    os.remove("utk.txt")
else:
    print("file doesn't exist")
```

**Explanation:**

* Use `os.remove()` to delete.
* Always check with `os.path.exists()`.

---

### 📋 Copying Content from One File to Another

```python
with open("names.txt") as f:
    content = f.read()

with open("more_names.txt", "a") as f:
    f.write(content)
```

**Explanation:**

* First reads content.
* Then appends it to `more_names.txt`.

---

### 🧾 Writing Multi-line Text

```python
with open("notes.txt", "w") as f:
    f.write("""my name is utkarsh.\nI am 21 years old.\nI am thinking about reading the book Psycho-Cybernetics.""")
```

**Explanation:**

* Triple quotes for multi-line strings.

---

### 📚 Writing Using List of Strings

```python
lines = [
    "my name is utkarsh.\n",
    "I am 21 years old.\n",
    "I am thinking about reading the book Psycho-Cybernetics.\n"
]
with open("notes.txt", "w") as f:
    f.writelines(lines)
```

**Explanation:**

* `.writelines()` writes list of strings as-is.

---

### 🧮 Counting Lines in a File

```python
with open("notes.txt") as f:
    print(len(f.readlines()))
```

**Explanation:**

* `.readlines()` returns list of all lines.
* `len()` gives total number of lines.

---

### 🔍 Searching in File

```python
with open("notes.txt") as f:
    for line in f:
        if "cybernetics" in line.lower():
            print("Found:", line.strip())
```

**Explanation:**

* Searches for word "cybernetics" ignoring case.

---

### 🔢 Count Word Occurrences

```python
count = 0
with open("notes.txt") as f:
    for line in f:
        count += line.lower().count("am")
print("Total 'am' characters:", count)
```

**Explanation:**

* Counts how many times "am" appears in the file.

---

### 🖨️ Print Specific Lines

```python
with open("notes.txt") as file:
    for i in range(2):
        print(file.readline().strip())
```

**Explanation:**

* Reads and prints first 2 lines.

---

### 🔚 Print First and Last Line

```python
with open("notes.txt") as f:
    lines = f.readlines()
print(lines[0].strip())      # First line
print(lines[-1].strip())     # Last line
```

**Explanation:**

* First and last line using indexing.

---

### 💡 Writing Multiple Lines to New File

```python
lines = ["line 1\n", "line 2\n", "line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

**Explanation:**

* Writes predefined lines to a file.

---

### 📏 Longest Line in a File

```python
with open("sample.txt") as f:
    lines = f.readlines()

longest_line = max(lines, key=len)
print(longest_line.strip(), ":", len(longest_line.strip()))
```

**Explanation:**

* Finds line with max length using `key=len`.
* Strips and prints it with its length.

---

### 🔑 Bonus: Understanding `key=` Argument

**`key=`** is used with `max()`, `min()`, and `sorted()` to customize how comparison is done:

#### 🧮 Examples:

```python
words = ["apple", "Banana", "pear"]
print(sorted(words, key=str.lower))  # case-insensitive
```

```python
names = ["Sam", "Bob", "Alex"]
print(sorted(names, key=lambda x: x[-1]))  # last char sort
```

```python
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
print(sorted(people, key=lambda x: x[1]))  # by age
```

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

students = [Student("Alice", 85), Student("Bob", 92)]
topper = max(students, key=lambda s: s.grade)
print(topper.name)
```

---


* Use `open()` or `with open()` to read/write files.
* Always close files or use `with` block.
* Use modes like `r`, `w`, `a`, `x` depending on task.
* `key=` argument is powerful for custom sorting or filtering.

📁 File handling is a **core part of real-world Python programming** — for logs, configs, saving data, backups, etc.

</details>

<details>

 <summary> ☁️ Lab 8</summary>

### 🌍 Topic: Weather API Project with Environment Variables and External Packages

---

### 🔌 What is an API?

**API (Application Programming Interface)** allows different software systems to communicate with each other.

In this lab, we use the **OpenWeatherMap API** to get live weather data for any city by making an HTTP request.

```python
https://api.openweathermap.org/data/2.5/weather
```

We attach **query parameters** like:

* `q=cityname` – for city input
* `appid=your_api_key` – unique API key (kept secret)
* `units=metric` – temperature in Celsius

---

### 📦 What are Packages?

**Packages** are collections of Python modules. Here, we use:

* `requests` – to send HTTP requests to the weather API
* `dotenv` – to securely manage sensitive info like the API key
* `os` – to access environment variables
* `pprint` – to print JSON data nicely (optional)

> You install them using `pip install requests python-dotenv`

---

### 🧪 Example Code Walkthrough

```python
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

# Function to fetch current weather for user-entered city
def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ").replace(" ", "+")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    print(f'\nCurrent weather for {weather_data["name"]}.')
    print(f'\nThe temperature is  {weather_data["main"]["temp"]}.')
    print(f'\nFeels like  {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')

# Only run the function if this is the main file
if __name__ == "__main__":
    get_current_weather()
```

### 🖥️ Output:

```
Please enter a city name: Mumbai

Current weather for Mumbai.
The temperature is  30.2.
Feels like  34.6 and haze.
```

---

### 🗃️ .env File and dotenv

`.env` is a simple file used to store environment variables locally.
It is **not pushed to GitHub** to protect secrets.

```dotenv
API_KEY=your_openweathermap_api_key_here
```

* Use `load_dotenv()` to load these variables into your Python script.
* Access them via `os.getenv("API_KEY")`

---

### 💻 os Module

The `os` module provides access to operating system functionalities like environment variables, file paths, etc.

```python
os.getenv("API_KEY")
```

---

### 🧪 Virtual Environments (`venv`)

A **virtual environment** is an isolated Python environment for your project.
It ensures that dependencies do not interfere across projects.

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

---

### 📄 `requirements.txt`

This file lists all the packages your project needs.
You generate it using:

```bash
pip freeze > requirements.txt
```

Install packages later using:

```bash
pip install -r requirements.txt
```

**Example:**

```
requests
python-dotenv
```

---



* ✅ Use APIs to fetch external data like weather
* 🔐 Store secrets securely using `.env`
* 📦 Install packages like `requests`, `dotenv`
* 🧪 Use `venv` to manage dependencies
* 📄 Track dependencies with `requirements.txt`

---


</details>

<details>
 <summary>🌤️ Lab 9</summary>

### 🌤️ Topic: Weather API Web App using Flask
---

### 🧩 Concepts Used

#### 📦 `requests`

Used to make HTTP requests to external APIs (like OpenWeatherMap) and handle responses in JSON format.

#### 🔐 `dotenv`

Used to load sensitive API keys from a `.env` file to avoid hardcoding them into the source code.

```python
from dotenv import load_dotenv
load_dotenv()
```

#### 🗝️ `os.getenv()`

Access environment variables securely using Python's `os` module.

```python
os.getenv("API_KEY")
```

#### 🌐 Flask

Flask is a lightweight web framework for building web applications in Python.

| Feature              | Description                                    |
| -------------------- | ---------------------------------------------- |
| `Flask`              | Main web framework                             |
| `render_template()`  | Renders HTML templates using Jinja2 templating |
| `@app.route()`       | Creates URL routes (like `/`, `/weather`)      |
| `request.args.get()` | Gets query parameters from the URL             |

#### ⚙️ Waitress

Production-ready WSGI server used to serve Flask applications more reliably than the default dev server.

```python
from waitress import serve
serve(app, host="0.0.0.0", port=8000)
```

#### 📁 `templates/` & `static/`

* HTML files are stored in the `templates` folder.
* CSS and images are in the `static` folder.
* Flask uses **Jinja2** syntax in HTML files (`{{ ... }}`) to inject dynamic data.

---

### 🧪 Example 1: `weather.py` - API Integration

```python
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="kolkata"):
    if not bool(city.strip()):
        city = "kolkata"

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()
    if weather_data['cod'] == 200:
        return weather_data
    else:
        return False
```

**Explanation:**

* Loads environment variables using `dotenv`
* Sends an HTTP request to the OpenWeatherMap API
* Returns weather data as a dictionary if the city is valid, else returns `False`

**Sample Output:**

```
{'name': 'Kolkata', 'main': {'temp': 32, 'feels_like': 34}, 'weather': [{'description': 'clear sky'}]}
```

---

### 🌐 Example 2: `server.py` - Flask Web Server

```python
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city or "kolkata")

    if not weather_data:
        return render_template("city_not_found.html")

    return render_template(
        "weather.html",
        title=weather_data['name'],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
```

**Explanation:**

* Sets up routing for the homepage and `/weather`
* Gets user input from query string and uses it to fetch weather data
* Displays formatted data in the web page using templates
* Uses `waitress` to serve the app in production mode

---

### 🧾 Templates

#### 🏠 `index.html`

```html
<form action="/weather">
  <input type="text" name="city" placeholder="kolkata" />
  <button type="submit">Get Weather</button>
</form>
```

Displays a form to get the city input from the user.

#### 🌡️ `weather.html`

```html
<h1>{{ title }} Weather</h1>
<p>{{ status }} and {{ temp }} °</p>
<p>Feels like {{ feels_like }} °</p>
```

Displays weather results dynamically using Jinja2 placeholders.

#### ❌ `city_not_found.html`

```html
<h1>City not found</h1>
<h4>Try Again?</h4>
```

Displays a user-friendly message if the entered city is not found.

---

### 📜 `requirements.txt`

Tracks all required packages for the project:

```
Flask
requests
python-dotenv
waitress
```

Use this file to set up the environment:

```bash
pip install -r requirements.txt
```

---

### 🌱 Virtual Environment (venv)

To isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

---

### 💡 HTML Template Notes

| Mode          | Example                                                                  |
| ------------- | ------------------------------------------------------------------------ |
| Plain HTML    | `<link href="style.css" rel="stylesheet">`                               |
| Flask + Jinja | `<link href="{{ url_for('static', filename='styles/style.css') }}" ...>` |

🔹 `{{ ... }}` - Jinja2 syntax for inserting Python variables into HTML
🔹 `url_for()` - Safely links to static files like CSS or JS

---

### 🎯 f-String Formatting Options in Python

| Format  | Description               | Example Output  |
| ------- | ------------------------- | --------------- |
| `.2f`   | 2 decimal places          | `'3.14'`        |
| `:>10`  | Right-align in 10 spaces  | `'     hello'`  |
| `:<10`  | Left-align                | `'hello     '`  |
| `:^10`  | Center-align              | `'  hello   '`  |
| `:,`    | Comma separator           | `'1,000'`       |
| `:_`    | Underscore separator      | `'1_000'`       |
| `.1%`   | Percentage format         | `'25.0%'`       |
| `b`     | Binary                    | `'1010'`        |
| `x / X` | Hexadecimal (lower/upper) | `'ff'` / `'FF'` |
| `.2e`   | Scientific notation       | `'1.23e+04'`    |

💡 Combine them like:

```python
f"{1234.56789:>10,.2f}"  # ➜ '  1,234.57'
```

---

### 🧠 Summary Table

| Concept            | Use Case                                      |
| ------------------ | --------------------------------------------- |
| `requests`         | Get data from APIs                            |
| `.env` & `os`      | Securely store and access API keys            |
| `Flask`            | Web framework to handle routing and templates |
| `waitress`         | Production-ready server for Flask apps        |
| `templates`        | Folder for dynamic HTML rendering (Jinja2)    |
| `static`           | Folder for CSS/images (linked in templates)   |
| `f-strings`        | Format strings with precision and style       |
| `requirements.txt` | Track project dependencies for setup          |
| `venv`             | Create isolated Python environments           |

---


</details>
