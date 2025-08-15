"""
Working with Directories in Python
---------------------------------
Use os module to create, remove, and navigate directories.
"""

import os

# Current working directory
cwd = os.getcwd()
print("Current directory:", cwd)

# List files and directories
print("Contents:", os.listdir('.'))

# Create a new directory
os.makedirs("test_folder", exist_ok=True)
print("Directory 'test_folder' created.")

# Check if directory exists
if os.path.exists("test_folder"):
    print("'test_folder' exists.")

# Remove directory
# os.rmdir("test_folder")  # Uncomment to remove the directory

# Change current working directory
os.chdir("..")
print("Changed directory to:", os.getcwd())

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a directory named 'my_folder' and verify it exists.
# 2. Create multiple nested directories.
# 3. List all files in the current directory.
# 4. Change directory to parent folder and print current directory.
