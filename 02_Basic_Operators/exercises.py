"""
Practice Exercises - Basic Operators
------------------------------------
Solve these exercises to understand arithmetic, comparison, and logical operators in Python.
"""

# ---------------------------
# Exercise 1: Arithmetic Operators
# ---------------------------
a = 10
b = 3

# 1. Perform addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# 2. Increment and decrement a variable using shorthand operators.
num = 5
num += 2  # increment by 2
print("Incremented:", num)
num -= 3  # decrement by 3
print("Decremented:", num)

# ---------------------------
# Exercise 2: Comparison Operators
# ---------------------------
x = 7
y = 10

# 1. Compare x and y using all comparison operators
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# ---------------------------
# Exercise 3: Logical Operators
# ---------------------------
# 1. Combine boolean expressions using and, or, not
p = True
q = False

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# 2. Check logical operations with comparison expressions
print("(x < y) and (y > 5):", (x < y) and (y > 5))
print("(x > y) or (y == 10):", (x > y) or (y == 10))

# ---------------------------
# Exercise 4: Extra Practice
# ---------------------------
# 1. Ask user for two numbers and perform all arithmetic operations.
# 2. Ask user for two numbers and check all comparison operators.
# 3. Combine logical operators in a single if-statement and print the result.
# 4. Experiment with operator precedence and parentheses.
