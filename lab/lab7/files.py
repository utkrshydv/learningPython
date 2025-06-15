# r = read
# a = append
# w = write
# x = create
import os
# read


f = open("names.txt", "r")  # rt - > read text file
# rb - > read binary file

# print(f.read())
# print(f.read(7))
# when we run both the commands, the first command reads all the names and then read(4) reads the next 4 characterrs

# read first line of file
# print(f.readline())

# for line in f:
#     print(line)

# f.close() #closes the opened file

# try:
#     f = open("names23.txt")
#     print(f.read())
# except:
#     print("file doesnt exist")
# finally:
#     f.close()

# append -> creates file if it doesnt exist

# f = open("names.txt", "a")
# f.write("utkarsh6")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

# write -> overwrite

# f = open("names.txt", "w")
# f.write("deleted everything")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

# ways to create a new file

# open a file for writing -> creates a neew file if it doesnt exist

# creates the specified file, but returns error if the file already exists so we import os

# if not os.path.exists("utk.txt"):
#     f = open("utk.txt", "x")
#     f.close()
# else:
#     print("already exists")


# delete a file


# needs to check if the file exists

# if os.path.exists("utk.txt"):
#   os.remove("utk.txt")
# else:
#   print("file doesnt exist")


# more conventional way files are handled

with open("names.txt") as f:
    content = f.read()

with open("more_names.txt", "a") as f:
    f.write(content)


with open("more_names.txt") as f:
    print(f.read())

#using with automatically handles file closing