"""
Decorators in Python
-------------------
Functions that modify the behavior of another function.
"""

# Basic decorator
def decorator_func(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# Function to decorate
def say_hello():
    print("Hello!")

# Applying decorator
decorated_function = decorator_func(say_hello)
decorated_function()

# Using @ syntax
@decorator_func
def greet():
    print("Greetings!")

greet()

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a decorator that prints 'Start' and 'End' around a function.
# 2. Create a decorator that measures execution time of a function.
# 3. Apply multiple decorators to a single function.
