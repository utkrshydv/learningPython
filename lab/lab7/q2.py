# # with open("sample.txt") as f:
# #     content = f.read().split()

# # print(len(content))


# # with open("sample.txt") as f:
# #     content = f.read()

# # with open("backup.txt", "w") as f:
# #     f.write(content)

# # with open("backup.txt") as f:
# #     print(f.read())


# # with open("sample.txt") as f:
# #     count = 1
# #     for line in f:
# #         print(f"{count}: {line}")
# #         count += 1

# with open("sample.txt") as f:
#     lines = f.readlines()

# longest_line = max(lines, key=len)

# print((longest_line), " : ", len(longest_line.strip()))


# #notes from chatgpt

# Excellent curiosity! In Python, the `key=` argument in functions like `max()`, `min()`, `sorted()`, etc., lets you **customize how elements are compared** — not just by length (`len`), but by **any function** that returns a value to compare.

# ---

# ### 🔑 Common Things You Can Use as `key`:

# #### 1. **Built-in functions**

# | Function       | Use Case                                      |
# | -------------- | --------------------------------------------- |
# | `len`          | Compare by length                             |
# | `abs`          | Compare by absolute value                     |
# | `str.lower`    | Case-insensitive comparison                   |
# | `int`, `float` | When elements are string numbers like `"100"` |

# ```python
# words = ["apple", "Banana", "pear"]
# print(sorted(words, key=str.lower))  # case-insensitive sort
# ```

# ---

# #### 2. **Custom Functions**

# You can define your own logic:

# ```python
# def last_char(s):
#     return s[-1]

# names = ["Sam", "Bob", "Alex"]
# print(sorted(names, key=last_char))  # Sort by last character
# ```

# ---

# #### 3. **Lambda Functions (short inline functions)**

# These are great for quick one-liners:

# ```python
# names = ["utkarsh", "bob", "alex"]
# print(sorted(names, key=lambda name: name.count('a')))  # Sort by number of 'a's
# ```

# ---

# #### 4. **Key for Tuples/Lists/Objects**

# When working with tuples, dictionaries, or objects:

# ```python
# people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
# # Sort by age
# print(sorted(people, key=lambda x: x[1]))  
# ```

# Or even:

# ```python
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

# students = [Student("Alice", 85), Student("Bob", 92)]
# topper = max(students, key=lambda s: s.grade)
# print(topper.name)
# ```

# ---

# ### 🧠 Summary

# The `key` argument is super powerful. It can take:

# * Any **function** that returns a value for comparison
# * Built-ins like `len`, `abs`, `str.lower`
# * Custom or lambda functions
# * Attribute or element access in complex data

