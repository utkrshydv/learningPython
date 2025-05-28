my_set = {1, 2, 3}
print(my_set)

nums = {1, 2, 3, 3, 4}
print(nums)

nums.add(5)
print(nums)

nums.remove(2)
print(nums)

print(3 in nums)

a = {1, 2, 3}
b = {4, 5, 6}
print(a | b)
c = a | b
print(c)

a = {1, 2, 3}
b = {2, 3, 6}
print(a & b)
c = a & b
print(c)
print(a-b)
print(a ^ b)

set1 = {1, 2, 3, 4}
set1.add(5)
set1.add(6)

x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

print(x | y)  # {1,2,3,4,5,6}
print(x & y)  # {3,4}
print(x-y)  # {1,2}
print(y-x)  # {5,6}
print(x ^ y)  # {1,2,5,6}
