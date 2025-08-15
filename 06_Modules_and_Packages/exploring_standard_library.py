"""
Exploring the Standard Library in Python
----------------------------------------
Python provides many built-in modules for various tasks.
"""

# os module - working with directories
import os
print("Current working directory:", os.getcwd())
print("List of files:", os.listdir('.'))

# datetime module - working with dates and times
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year, "Month:", now.month, "Day:", now.day)

# random module - generating random numbers
import random
print("Random float between 0 and 1:", random.random())
print("Random choice from list:", random.choice([1, 2, 3, 4, 5]))

# math module - mathematical operations
import math
print("Cosine of 0:", math.cos(0))
print("Ceil of 4.2:", math.ceil(4.2))

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Use os module to create a new folder and delete it.
# 2. Use datetime module to print current time in format HH:MM:SS.
# 3. Generate a random integer between 50 and 100 using random module.
# 4. Use math module to calculate the factorial of 7.
