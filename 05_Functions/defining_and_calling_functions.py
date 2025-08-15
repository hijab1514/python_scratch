"""
Defining and Calling Functions in Python
----------------------------------------
Functions are reusable blocks of code that perform a specific task.
"""

# Defining a simple function
def greet():
    print("Hello, welcome to Python functions!")

# Calling the function
greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Fatima")

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("Sum:", result)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Define a function that prints your name.
# 2. Define a function that takes two numbers and prints their product.
# 3. Call the functions multiple times with different arguments.
