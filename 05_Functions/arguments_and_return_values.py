"""
Arguments and Return Values in Python Functions
-----------------------------------------------
Functions can accept arguments and return values.
"""

# Positional arguments
def multiply(a, b):
    return a * b

print("Multiply 3 and 4:", multiply(3, 4))

# Default arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Fatima")

# Keyword arguments
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(age=21, name="Fatima")

# Return statement
def square(num):
    return num ** 2

print("Square of 5:", square(5))

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a function that returns the cube of a number.
# 2. Define a function with default arguments and call it with/without parameters.
# 3. Use keyword arguments to call a function with multiple parameters.
