"""
Custom Exceptions in Python
---------------------------
Create your own exceptions by extending the Exception class.
"""

# Define a custom exception
class NegativeNumberError(Exception):
    def __init__(self, message="Number cannot be negative"):
        self.message = message
        super().__init__(self.message)

# Function that raises custom exception
def check_positive(num):
    if num < 0:
        raise NegativeNumberError
    else:
        print("Number is positive:", num)

# Testing custom exception
try:
    number = int(input("Enter a number: "))
    check_positive(number)
except NegativeNumberError as e:
    print("Error:", e)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a custom exception for age validation (<0 or >120).
# 2. Raise custom exception if a string is empty.
# 3. Combine custom exceptions with try-except-finally.
