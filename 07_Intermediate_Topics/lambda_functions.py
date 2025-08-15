"""
Lambda Functions in Python
--------------------------
Anonymous, one-line functions defined using the 'lambda' keyword.
"""

# Basic lambda function
square = lambda x: x**2
print("Square of 5:", square(5))

# Lambda with multiple arguments
add = lambda a, b: a + b
print("Sum of 3 and 7:", add(3, 7))

# Lambda inside sorted()
numbers = [(1, 2), (3, 1), (5, 0)]
sorted_numbers = sorted(numbers, key=lambda x: x[1])
print("Sorted by second element:", sorted_numbers)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a lambda function to cube a number.
# 2. Use lambda to filter even numbers from a list.
# 3. Sort a list of tuples based on the first element using lambda.
