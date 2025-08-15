"""
Reading and Writing Files in Python
-----------------------------------
Python provides built-in functions to read from and write to files.
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a sample file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppended line.")

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a file and write your name and age into it.
# 2. Read the file content and print it.
# 3. Append another line with your favorite hobby.
# 4. Read the file line by line and print each line in uppercase.
