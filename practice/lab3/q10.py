# def reverse_list(my_list):
#   return my_list[::-1]


# def get_first_three_items(my_list):
#   return my_list[:3]

# def get_last_two_items(my_list):
#   return my_list[-2:]

# def skip_every_other_item(my_list):
#   return my_list[::2]

# def get_sublist_in_reverse(my_list):
#   return my_list[-3:0:-1]


# # Awesome! Here are 6 mini **slicing challenges** to test your skills — try them out and I’ll check your answers when you're ready!

# # ---

# # ### 🧩 **Challenge 1: First 4 items**

# # ```python
# # nums = [10, 20, 30, 40, 50, 60]
# # # Get: [10, 20, 30, 40]
# # ```
#  return [:4]
# # ---

# # ### 🧩 **Challenge 2: All except first and last**

# # ```python
# # nums = [1, 2, 3, 4, 5]
# # # Get: [2, 3, 4]
# # ```
#  return [1:4]
# # ---

# # ### 🧩 **Challenge 3: Reverse only first 3**

# # ```python
# # nums = [100, 200, 300, 400, 500]
# # # Get: [300, 200, 100]
# # ```

# return [::-1][2:5]

# # ---

# # ### 🧩 **Challenge 4: Last 3 items, in reverse**

# # ```python
# # nums = [5, 10, 15, 20, 25, 30]
# # # Get: [30, 25, 20]
# # ```
#  return [::-1][:3]
# # ---

# # ### 🧩 **Challenge 5: Every 2nd element starting from index 1**

# # ```python
# # nums = [0, 1, 2, 3, 4, 5, 6]
# # # Get: [1, 3, 5]
# # ```
# return [1::2]

# # ---

# # ### 🧩 **Challenge 6: Copy the list**

# # ```python
# # nums = [7, 8, 9]
# # # Get: [7, 8, 9] (not the original reference)
# # ```
# return [:]
# # ---

# # Reply with your answers and I’ll review each one!

# # Sure! Here are some tailored practice questions focusing on the concepts you missed or got confused with—mainly slicing and reversing parts of lists:

# # ---

# # ### 🔹 **Practice Question 1:**

# # Given a list, return the middle part **excluding the first and last elements**.

# # ```python
# # # Example:
# # lst = [5, 10, 15, 20, 25, 30]
# # # Output: [10, 15, 20, 25]
# # ```
#  return lst[1:-1]
# # ---

# # ### 🔹 **Practice Question 2:**

# # Reverse the **first 4 elements** of a list, but keep the rest as is.

# # ```python
# # # Example:
# # lst = [1, 2, 3, 4, 5, 6]
# # # Output: [4, 3, 2, 1, 5, 6]
# # ```
# return lst[:4:-1].append(lst[4:6])
# # ---

# # ### 🔹 **Practice Question 3:**

# # Return the **last 4 elements** of the list in reverse order.

# # ```python
# # # Example:
# # lst = [11, 22, 33, 44, 55, 66, 77]
# # # Output: [77, 66, 55, 44]
# # ```
# return lst[-1:-4]
# # ---

# # ### 🔹 **Practice Question 4:**

# # Return every **3rd element**, starting from the second element (index 1).

# # ```python
# # # Example:
# # lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # Output: [1, 4, 7]
# # ```
# return lst[1::3]
# # ---

# # ### 🔹 **Practice Question 5:**

# # Copy the entire list but **exclude the last two elements**.

# # ```python
# # # Example:
# # lst = [100, 200, 300, 400, 500]
# # # Output: [100, 200, 300]
# # ```
# return lst[:-2]
# # ---

# # Try these out, and I’ll review your solutions! Want me to give you hints too?


# Sure! Here are 4 focused practice questions to help you master list slicing and reversing — especially those tricky parts you struggled with:

# ---

# # ### 1. Return the **first 5 elements** of a list in **reverse order**.

# # ```python
# # # Example:
# # lst = [10, 20, 30, 40, 50, 60, 70]
# # # Output: [50, 40, 30, 20, 10]
# # ```
# return lst[:5][::-1]
# # ---

# # ### 2. Return a list containing elements from index 3 up to (but **not including**) index 7.

# # ```python
# # # Example:
# # lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# # # Output: [3, 4, 5, 6]
# # ```

# return lst[3:7]

# # ---

# # ### 3. Return the last 5 elements of the list, **in normal order**.

# # ```python
# # # Example:
# # lst = [5, 10, 15, 20, 25, 30, 35, 40]
# # # Output: [20, 25, 30, 35, 40]
# # ```
# return lst[-5:-1]
# # ---

# # ### 4. Return every 3rd element of the list, starting from index 2.

# # ```python
# # # Example:
# # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# # # Output: [3, 6, 9]
# # ```
# return lst[2::3]
# # ---

# # Try these out and send me your answers! I’ll check them and explain anything that needs clarity. Want me to provide hints too?


# Awesome! Let’s do a final revision round on slicing with some fresh questions that cover all key cases — positive/negative indexes, steps, reverse, partial slices, etc. Try these out and share your answers:

# ---

# ### 🔹 **Revision Question 1:**

# Return the **first 3 elements** of a list.

# ```python
# lst = [11, 22, 33, 44, 55, 66]
# # Expected output: [11, 22, 33]
# ```
# returb lst[:3]
# ---

# ### 🔹 **Revision Question 2:**

# Return the **last 4 elements** of a list.

# ```python
# lst = [10, 20, 30, 40, 50, 60, 70]
# # Expected output: [40, 50, 60, 70]
# ```
# return lst[-4:]
# ---

# ### 🔹 **Revision Question 3:**

# Return the list in **reverse order**.

# ```python
# lst = [1, 2, 3, 4, 5]
# # Expected output: [5, 4, 3, 2, 1]
# ```
# return [::-1]
# ---

# ### 🔹 **Revision Question 4:**

# Return **every 2nd element** of the list, starting from the first element (index 0).

# ```python
# lst = [0, 1, 2, 3, 4, 5, 6]
# # Expected output: [0, 2, 4, 6]
# ```
# return lst[::2]
# ---

# ### 🔹 **Revision Question 5:**

# Return the list excluding the **first and last elements**.

# ```python
# lst = [10, 20, 30, 40, 50]
# # Expected output: [20, 30, 40]
# ```
# return lst[1:-1]
# ---

# ### 🔹 **Revision Question 6:**

# Return a slice containing elements from index 2 up to index 5 (exclusive).

# ```python
# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# # Expected output: ['c', 'd', 'e']
# ```
# return lst[2:5]
# ---

# ### 🔹 **Revision Question 7:**

# Return every 3rd element of the list, starting from the second element (index 1).

# ```python
# lst = [5, 10, 15, 20, 25, 30, 35, 40]
# # Expected output: [10, 25, 40]
# ```
# return lst[1::3]
# ---

# ### 🔹 **Revision Question 8:**

# Copy the entire list using slicing.

# ```python
# lst = [7, 8, 9]
# # Expected output: [7, 8, 9] (a new list, not reference)
# ```
# return lst[:]
# ---

# Try to write the slicing expressions (only the part inside brackets, like `lst[...]`) for each question.

# Send me your answers and I’ll review! Ready?


# Awesome! Here's your **final slicing challenge** to combine everything you've learned — reversing, skipping, indexing, and slicing ranges.

# ---

# ### 🌟 **Ultimate Slicing Challenge**

# You’re given the list:

# ```python
# lst = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# ```

# Write the slicing expression (just `lst[...]`) for each task:

# ---

# #### 🔹 **Q1: Get the last 3 elements in reverse order**

# ✅ Expected output: `[50, 45, 40]`
# lst[-1:-4:-1]
# ---

# #### 🔹 **Q2: Skip every other element from the list (starting at index 0)**

# ✅ Expected output: `[5, 15, 25, 35, 45]`
# lst[::2]
# ---

# #### 🔹 **Q3: Get elements from index 2 to index 7 (inclusive), in reverse**

# ✅ Expected output: `[40, 35, 30, 25, 20, 15]`
# lst[2:8][::-1]
# ---

# #### 🔹 **Q4: Copy the list but exclude the first 2 and last 2 elements**

# ✅ Expected output: `[15, 20, 25, 30, 35, 40]`
# lst[2:-2]
# ---

# #### 🔹 **Q5: Reverse the entire list and then return every 3rd item from the reversed list**

# ✅ Expected output: `[50, 35, 20, 5]`
# lst[::-1][::3]
# ---

# Try writing the slicing expression (`lst[...]`) for each — then I’ll check and explain any tricky ones!
