"""
Tuples in Python
----------------
Ordered, immutable collections of items. Can contain duplicates.
"""

# Creating tuples
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)

print("Fruits tuple:", fruits)
print("Numbers tuple:", numbers)

# Accessing elements
print("First fruit:", fruits[0])
print("Last number:", numbers[-1])

# Slicing
print("Slice numbers[1:4]:", numbers[1:4])

# Tuples are immutable
# fruits[0] = "orange"  # ❌ This will raise an error

# Tuple operations
combined = fruits + ("orange", "kiwi")
print("Combined tuple:", combined)
print("Repetition:", numbers * 2)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a tuple of 5 elements and access the third element.
# 2. Slice a tuple to get the last 2 elements.
# 3. Combine two tuples and print the result.
# 4. Try changing an element and observe the error.
