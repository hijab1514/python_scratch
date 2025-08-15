"""
List Comprehensions in Python
-----------------------------
Concise way to create lists using a single line of code.
"""

# Basic example
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# Nested loop
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print("Pairs:", pairs)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a list of cubes from 1 to 10 using list comprehension.
# 2. Create a list of numbers divisible by 3 from 1 to 20.
# 3. Generate all combinations of two lists using nested list comprehension.
