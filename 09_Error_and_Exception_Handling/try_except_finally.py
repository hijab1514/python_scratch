"""
Try, Except, Finally in Python
------------------------------
Used to handle errors and exceptions gracefully.
"""

# Basic try-except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")

# Multiple exceptions
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = x / y
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter integers.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Finally block
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution finished.")

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Ask user for a number and handle non-integer inputs.
# 2. Divide two numbers and handle division by zero.
# 3. Open a file and handle the case when file does not exist.
# 4. Experiment with try-except-finally blocks in different scenarios.
