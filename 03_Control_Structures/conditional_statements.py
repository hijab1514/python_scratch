"""
Conditional Statements in Python
--------------------------------
Used to execute code based on certain conditions.
"""

# Single if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# if-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")

# Nested if statement
a = 8
if a > 0:
    if a % 2 == 0:
        print("a is positive and even")
    else:
        print("a is positive and odd")

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Ask user for a number and check if it is positive, negative, or zero.
# 2. Check if a number is divisible by 3 and 5.
# 3. Create a grading system using if-elif-else.
# 4. Nest multiple conditions to check for even/odd and positive/negative.
