# Given this dictionary
students = {
    'Alice': 85,
    'Bob': 72,
    'Charlie': 90
}

# 1. Add a new student 'David' with grade 88
# 2. Increase Bob’s grade by 5
# 3. Print each student and their updated grade
students['David'] = 88
students['Bob'] = students['Bob'] + 5
print(students)

sentence = "python is great and python is fun"

# Count how many times each word appears
# Output: {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}
words = sentence.split(" ")

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


# Each student has multiple subject scores
students = {
    'Utkarsh': {'Math': 95, 'Science': 88},
    'Disha': {'Math': 100, 'Science': 92},
    'Rohit': {'Math': 70, 'Science': 65}
}

# 1. Print each student's average score
# 2. Find who has the highest Math score

for key in students.keys():
    avg = (students[key]['Math'] + students[key]['Science']) / 2
    print(avg)

marks_in_maths = []

for value in students.values():
    marks_in_maths.append(value['Math'])

print(max(marks_in_maths))


# Build a phonebook dictionary with names and numbers
phonebook = {
    'Mom': '9876543210',
    'Dad': '8765432109',
    'Friend': '7654321098'
}

# 1. Ask user to enter a name
# 2. Print the number if name exists, else say "Not found"
name = input("Enter a name: ")

print(phonebook.get(name, "Not found"))

inventory = {
    'apple': 10,
    'banana': 5,
    'orange': 7
}

# 1. A customer buys 2 bananas and 1 orange
inventory['banana'] -= 2
inventory['orange'] -= 1
# 2. Update the inventory
print(inventory)
# 3. Add a new item 'grapes' with quantity 15
inventory['grapes'] = 15
# 4. Print the final inventory
print(inventory)
