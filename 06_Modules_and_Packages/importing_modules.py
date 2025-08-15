"""
Importing Modules in Python
---------------------------
Modules are files containing Python code (functions, variables, classes)
that can be imported and used in other programs.
"""

# Importing entire module
import math
print("Square root of 16:", math.sqrt(16))

# Importing specific functions
from math import factorial, pi
print("Factorial of 5:", factorial(5))
print("Value of pi:", pi)

# Importing with alias
import random as rnd
print("Random integer between 1 and 10:", rnd.randint(1, 10))

# Using sys module
import sys
print("Python version:", sys.version)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Import the math module and calculate power of a number.
# 2. Import only randint from random and print a random number between 1-100.
# 3. Import sys and print the path of Python interpreter.
