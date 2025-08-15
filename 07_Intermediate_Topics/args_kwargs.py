"""
*args and **kwargs in Python Functions
-------------------------------------
*args: for variable number of positional arguments
**kwargs: for variable number of keyword arguments
"""

# *args example
def add_numbers(*args):
    total = sum(args)
    print("Sum:", total)

add_numbers(1, 2, 3, 4)

# **kwargs example
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Fatima", age=21, major="CS")

# Combining normal, *args, and **kwargs
def combined(a, b, *args, **kwargs):
    print("a + b =", a + b)
    print("*args:", args)
    print("**kwargs:", kwargs)

combined(1, 2, 3, 4, city="Seoul", country="Korea")

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a function that takes any number of numbers and returns their product.
# 2. Create a function that prints key-value pairs of a dictionary using **kwargs.
# 3. Combine normal arguments, *args, and **kwargs in a single function.
