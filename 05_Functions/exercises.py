"""
Practice Exercises - Functions
------------------------------
Solve these exercises to practice defining functions, using arguments, return values, and variable scope.
"""

# ---------------------------
# Exercise 1: Basic Function
# ---------------------------
def say_hello():
    print("Hello!")

say_hello()

# ---------------------------
# Exercise 2: Function with Arguments
# ---------------------------
def add(a, b):
    return a + b

print("5 + 7 =", add(5, 7))

# ---------------------------
# Exercise 3: Function with Default and Keyword Arguments
# ---------------------------
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet(name="Fatima")

# ---------------------------
# Exercise 4: Local and Global Variables
# ---------------------------
x = 10  # Global variable

def func1():
    y = 5  # Local variable
    print("Inside func1, x =", x, "y =", y)

func1()
# print(y)  # ❌ Error: y is local

def func2():
    global x
    x += 5

print("Before func2, x =", x)
func2()
print("After func2, x =", x)

# ---------------------------
# Exercise 5: Extra Practice
# ---------------------------
# 1. Create a function that returns the factorial of a number.
# 2. Create a function that checks if a number is prime.
# 3. Create a function that takes a list and returns the sum of its elements.
