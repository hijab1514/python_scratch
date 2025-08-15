"""
Lists in Python
---------------
Ordered, mutable collections of items. Can contain duplicates.
"""

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

print("Fruits:", fruits)
print("Numbers:", numbers)

# Accessing elements
print("First fruit:", fruits[0])
print("Last number:", numbers[-1])

# Slicing
print("Slice fruits[1:]:", fruits[1:])

# Adding elements
fruits.append("orange")
print("After append:", fruits)

fruits.insert(1, "kiwi")
print("After insert at index 1:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

popped = fruits.pop()
print("Popped element:", popped)
print("Fruits after pop:", fruits)

# List operations
more_numbers = numbers + [6, 7, 8]
print("Concatenated list:", more_numbers)
print("Repetition:", fruits * 2)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a list of 5 numbers and print their sum.
# 2. Add a new item to a list and remove the second item.
# 3. Slice a list to get the first 3 elements.
# 4. Combine two lists and print the result.
