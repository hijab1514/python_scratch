"""
Practice Exercises - Error and Exception Handling
-------------------------------------------------
Solve these exercises to practice handling exceptions in Python.
"""

# ---------------------------
# Exercise 1: Try-Except
# ---------------------------
try:
    num = int(input("Enter a number: "))
    print("Number entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")

# ---------------------------
# Exercise 2: Division with Exception Handling
# ---------------------------
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = x / y
    print("Result:", result)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ---------------------------
# Exercise 3: File Handling Exception
# ---------------------------
try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist.")

# ---------------------------
# Exercise 4: Custom Exception
# ---------------------------
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    else:
        print("Valid age:", age)

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Error:", e)
