# lst = [1, 3, 5]
# lst.append(7)
# print(lst)
# lst.insert(1, 2)
# print(lst)
# lst.remove(3)
# lst.sort()
# print(lst)
# lst.reverse()
# print(lst)

# lst = []
# lst.append(1)
# lst.append(2)
# lst.append(3)
# print(lst)

# lst1 = [10, 20, 30]
# lst1.insert(1, 99)
# print(lst1)

# lst2 = [40, 50, 60, 70]
# lst2.remove(50)
# print(lst2)

# lst3 = [3, 1, 4, 2]
# lst3.sort()
# print(lst3)

# lst4 = [100, 200, 300]
# lst4.reverse()
# print(lst4)

# fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# print(fruits.count('apple'))

# colors = ['red', 'blue', 'green', 'blue', 'yellow']
# print(colors.index("blue"))

# numbers = [5, 10, 15]
# copy_numbers = numbers.copy()
# print(numbers)
# print(copy_numbers)
# copy_numbers.append(44)
# print(copy_numbers)
# print(numbers)
# numbers.append(69)
# print(numbers)
# print(copy_numbers)

# import copy

# # original = [[1, 2], [3, 4]]
# # shallow_copy = copy.copy(original)

# # print("Before Modification: ")
# # print("Original: ", original)
# # print("Shallow Copy: ", shallow_copy)

# # shallow_copy[0].append(99)

# # print("After Modifications: ")
# # print("Original: ", original)
# # print("Shallow Copy: ", shallow_copy)

# original = [[1, 2], [3, 4]]
# deep_copy = copy.deepcopy(original)

# print("Before modification:")
# print("Original:", original)
# print("Deep copy:", deep_copy)

# deep_copy[0].append(99)

# print("\nAfter modifying deep_copy[0]:")
# print("Original:", original)
# print("Deep copy:", deep_copy)


# lst = [10, 20, 30, 40]
# x = lst.pop()
# print(x)
# print(lst)


# lst = [5, 10, 15]
# print(lst.pop())

# lst.extend([20, 25])
# print(lst)

# lst_copy = lst.copy()
# print(lst_copy)

# lst = [10, 20, 30, 40, 50]
# print(lst.pop())
# print(lst.pop())

# lst1 = [1, 2, 3]
# lst2 = [4, 5]
# lst1.extend(lst2)
# print(lst1)

# original = ['a', 'b', 'c']
# copy_list = original.copy()
# copy_list.append('d')
# print(copy_list)


# lst = []
# lst.append(10)
# lst.append(20)
# lst.append(30)
# lst.insert(1, 15)

# print(lst)

# nums = [5, 10, 15, 20, 25]
# nums.remove(15)
# last_num = nums.pop()
# print(nums)
# print(last_num)

# words = ['yes', 'no', 'maybe', 'yes', 'yes']
# print(words.count('yes'))
# print(words.index('maybe'))

# colors = ['red', 'blue', 'green']
# copied_colors = colors.copy()
# copied_colors.append('yellow')
# print(colors)
# print(copied_colors)

# items = [1, 2]
# items.extend([3, 4, 5])
# print(items)

# items.reverse()
# print(items)


# nums = [2, 3, 4]
# result = list(map(lambda x: x*x, nums))
# print(result)

# words = ['hello', 'world']
# result2 = list(map(lambda x: x.upper(), words))
# print(result2)

# nums2 = [5, 10, 15]
# result3 = list(map(lambda x : x+5, nums2))
# print(result3)

# nums = [1, 2, 3, 4, 5, 6]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)

# words = ['hi', 'girl', 'you', 'lookin', 'nice']
# long_words = list(filter(lambda word: len(word) >= 5, words))
# print(long_words)

# nums = [-5, 3, -1, 0, 7, -9, 2]

# pos_nums = list(filter(lambda num: num > 0, nums))
# print(pos_nums)

# words = ['hello', '', 'world', '', 'python']
# not_empty = list(filter(lambda word: word != '', words))
# print(not_empty)

# nums2 = [3, 6, 10, 12, 15, 19]
# div_by_3 = list(filter(lambda x: x % 3 == 0, nums2))
# print(div_by_3yes)

# words2 = ['HELLO', 'World', 'YES', 'no', 'OK']
# only_upper = list(filter(lambda x: x.isupper(), words2))
# print(only_upper)

# nums = [1, 2, 3, 4, 5, 6, 7, 8]

# even = list(filter(lambda x: x % 2 == 0, nums))
# square_evens = list(map(lambda x: x*x,  even))
# print(square_evens)

# words = ['madam', 'hello', 'noon', 'python', 'level']

# palindromes = list(filter(lambda x:  x == x[::-1], words))
# upper_palindromes = list(map(lambda x: x.upper(), palindromes))
# print(upper_palindromes)

# nums = [3, 8, 11, 20, 7]

# odds = list(filter(lambda x: x % 2 != 0, nums))
# add_10 = list(map(lambda x: x+10, odds))
# print(add_10)

# words = ['python', 'java', 'perl', 'ruby', 'php']
# start_with_p = list(filter(lambda x: x[0] == 'p', words))
# get_length = list(map(lambda x: len(x), start_with_p))
# print(get_length)

# items = [0, 1, 2, '', None, 3, False, 4]
# no_falsy = list(filter(lambda x: x != 0 and x !=
#                 '' and x != None and x != False, items))
# square_them = list(map(lambda x: x*x, no_falsy))
# print(square_them)

# words = ['yes', 'hello', 'no', 'great', 'ok']
# larger = list(filter(lambda x: len(x) > 3, words))
# capitalize = list(map(lambda x: x.upper(), larger))
# print(capitalize)


# items = [0, 1, 2, '', None, 3, False, 4]
# no_falsy = list(filter(None, items))
# squared = list(map(lambda x : x*x, no_falsy))


# words = ['madam', 'hello', 'noon', 'python', 'level']
# upper_palindrome = [w.upper() for w in words if w == w[::-1]]
# print(upper_palindrome)

squared_nums = [i*i for i in range(1,11)]
print(squared_nums)

words = ['apple', 'banana', 'avocado', 'berry', 'apricot']
starts_with_a = [w for w in words if w[0] == 'a']
print(starts_with_a)

nums = [1, 2, 3, 4, 5, 6]
multiplied_by_2 = [x*2 for x in nums if x %2 == 0]
print(multiplied_by_2)

nums = [7, 2, 5, 8]
odd_even = ["even" if x%2==0 else "odd" for x in nums]
print(odd_even)





