"""
Logical Operators in Python
---------------------------
Used to combine conditional statements. Returns a boolean result.
"""

# Boolean variables
p = True
q = False

# AND operator
print("p and q:", p and q)

# OR operator
print("p or q:", p or q)

# NOT operator
print("not p:", not p)

# Logical operations with comparison
x = 5
y = 10

print("(x < y) and (y > 5):", (x < y) and (y > 5))
print("(x > y) or (y == 10):", (x > y) or (y == 10))
print("not (x == y):", not (x == y))

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Combine multiple logical operators in a single if-statement.
# 2. Ask user for two numbers and use logical operators to check conditions.
# 3. Try using 'and' and 'or' with non-boolean values and observe the result.
# 4. Experiment with 'not' on different expressions and print the output.
