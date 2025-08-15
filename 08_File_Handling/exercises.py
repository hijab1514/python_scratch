"""
Practice Exercises - File Handling
----------------------------------
Solve these exercises to practice reading, writing files, and working with directories.
"""

import os

# ---------------------------
# Exercise 1: Write and Read File
# ---------------------------
with open("my_file.txt", "w") as file:
    file.write("Name: Fatima\nAge: 21\nHobby: Coding")

with open("my_file.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# ---------------------------
# Exercise 2: Append File
# ---------------------------
with open("my_file.txt", "a") as file:
    file.write("\nFavorite Language: Python")

with open("my_file.txt", "r") as file:
    print("Updated content:\n", file.read())

# ---------------------------
# Exercise 3: Working with Directories
# ---------------------------
# Create a new directory
os.makedirs("practice_folder", exist_ok=True)
print("Directory 'practice_folder' created.")

# List contents
print("Current directory contents:", os.listdir('.'))

# Remove directory
# os.rmdir("practice_folder")  # Uncomment to remove

# ---------------------------
# Exercise 4: Extra Practice
# ---------------------------
# 1. Create a file named 'data.txt' and write 5 lines of data.
# 2. Read the file and count the number of lines.
# 3. Create a nested directory structure: 'folder1/folder2/folder3'.
# 4. Check if a specific file exists in the directory.
