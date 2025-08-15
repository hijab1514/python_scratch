"""
Sets in Python
--------------
Unordered, mutable collections of unique items. No duplicates allowed.
"""

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

print("Fruits set:", fruits)
print("Numbers set:", numbers)

# Adding elements
fruits.add("orange")
print("After add:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference a - b:", a - b)
print("Symmetric Difference:", a ^ b)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a set of numbers and add a new element.
# 2. Remove an element from a set.
# 3. Perform union and intersection on two sets.
# 4. Check if an element exists in a set.
