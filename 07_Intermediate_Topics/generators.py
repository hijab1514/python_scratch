"""
Generators in Python
-------------------
Functions that yield items one at a time using 'yield' keyword.
"""

# Basic generator
def simple_generator():
    for i in range(5):
        yield i

for value in simple_generator():
    print("Generated value:", value)

# Generator expression
squares = (x**2 for x in range(1, 6))
for s in squares:
    print("Square:", s)

# Infinite generator
def infinite_sequence(start=0):
    num = start
    while True:
        yield num
        num += 1

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a generator that yields even numbers up to 20.
# 2. Use a generator expression to create a sequence of cubes.
# 3. Write an infinite generator and use break to stop after 5 numbers.
