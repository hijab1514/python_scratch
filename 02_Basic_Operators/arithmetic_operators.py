"""
Arithmetic Operators in Python
------------------------------
Used to perform mathematical operations on numbers.
"""

# Variables
a = 10
b = 3

# Addition
sum_result = a + b
print("Addition: {} + {} = {}".format(a, b, sum_result))

# Subtraction
sub_result = a - b
print("Subtraction: {} - {} = {}".format(a, b, sub_result))

# Multiplication
mul_result = a * b
print("Multiplication: {} * {} = {}".format(a, b, mul_result))

# Division
div_result = a / b  # Returns float
print("Division: {} / {} = {}".format(a, b, div_result))

# Floor Division
floor_div = a // b  # Returns integer part
print("Floor Division: {} // {} = {}".format(a, b, floor_div))

# Modulus
mod_result = a % b  # Remainder
print("Modulus: {} % {} = {}".format(a, b, mod_result))

# Exponentiation
exp_result = a ** b
print("Exponentiation: {} ** {} = {}".format(a, b, exp_result))

# Increment and Decrement (using shorthand operators)
num = 5
num += 2  # Increment by 2
print("Incremented by 2:", num)
num -= 3  # Decrement by 3
print("Decremented by 3:", num)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create two variables and perform all arithmetic operations.
# 2. Experiment with negative numbers and floats.
# 3. Use parentheses to change the order of operations and print the result.
# 4. Combine multiple arithmetic operators in a single expression and check the result.
