"""
Practice Exercises - Modules and Packages
-----------------------------------------
Solve these exercises to practice importing modules and using the Python standard library.
"""

# ---------------------------
# Exercise 1: math module
# ---------------------------
import math

# Calculate square root
num = 25
print("Square root of", num, "is", math.sqrt(num))

# Calculate factorial
print("Factorial of 6 is", math.factorial(6))

# ---------------------------
# Exercise 2: random module
# ---------------------------
from random import randint, choice

# Random integer between 1 and 100
print("Random integer:", randint(1, 100))

# Random choice from list
items = ["apple", "banana", "cherry"]
print("Random choice:", choice(items))

# ---------------------------
# Exercise 3: datetime module
# ---------------------------
import datetime

now = datetime.datetime.now()
print("Current date:", now.date())
print("Current time:", now.time())

# ---------------------------
# Exercise 4: os module
# ---------------------------
import os

# Print current working directory
cwd = os.getcwd()
print("Current directory:", cwd)

# List files in current directory
print("Files in directory:", os.listdir('.'))

# ---------------------------
# Exercise 5: Extra Practice
# ---------------------------
# 1. Use math module to calculate cosine and sine of 45 degrees.
# 2. Use random module to shuffle a list.
# 3. Use datetime module to print the current weekday.
# 4. Use os module to check if a file exists in the current directory.
