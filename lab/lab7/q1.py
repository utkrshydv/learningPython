# | Mode  | Meaning                       |
# | ----- | ----------------------------- |
# | `"r"` | Read (default)                |
# | `"w"` | Write (overwrites file)       |
# | `"a"` | Append (adds to file)         |
# | `"x"` | Create (fails if file exists) |
# | `"b"` | Binary mode (images, etc.)    |
# | `"t"` | Text mode (default)           |
#

# with open("notes.txt", "w") as f:
#     f.write("my name is utkarsh. \n I am 21 years old. \n I am thinkinh about readind the book Psycho cybernetics ")


# with open("notes.txt") as f:
#     print(f.read())

# #way 2

# with open("notes.txt", "w") as f:
#     f.write("""my name is utkarsh.
# I am 21 years old.
# I am thinking about reading the book Psycho-Cybernetics.""")

# #way 3

# with open("notes.txt", "w") as f:
#     f.writelines([
#         "my name is utkarsh.\n",
#         "I am 21 years old.\n",
#         "I am thinking about reading the book Psycho-Cybernetics.\n"
#     ])


# with open("notes.txt", "a") as f:
#     f.write("\nlets see how file handling works in real life")

# f = open("notes.txt")

# count = 0
# for line in f:
#     count += 1

# print(count)

# # better way

# with open("notes.txt") as f:
#     print(len(f.readlines()))

# with open("notes.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# with open("notes.txt", "r") as file:
#     for i in range(2):
#         line = file.readline()
#         print(line.strip())

# with open("notes.txt", "r") as file:
#     lines = file.readlines()

# print(lines[0].strip())   # First line
# print(lines[-1].strip())  # Last line

# with open("notes.txt", "r") as f:
#     for line in f:
#         if "cybernetics" in line.lower():
#             print("Found: ", line.strip())


# count = 0
# with open("notes.txt", "r") as file:
#     for line in file:
#         count += line.lower().count("am")

# print("Total 'am' characters:", count)

# lines = ["line 1\n", "line 2\n", "line 3\n"]

# with open("output.txt", "w") as file:
#     file.writelines(lines)

# | Mode   | Meaning                     |
# | ------ | --------------------------- |
# | `"r"`  | Read (default)              |
# | `"w"`  | Write (overwrites file)     |
# | `"a"`  | Append                      |
# | `"r+"` | Read and Write              |
# | `"w+"` | Write and Read (overwrites) |


with open("notes.txt") as f:
    lines = f.readlines()

print(lines)
