"""
Practice Exercises - Basic Data Structures
------------------------------------------
Solve these exercises to practice Lists, Tuples, Sets, and Dictionaries.
"""

# ---------------------------
# Exercise 1: Lists
# ---------------------------
numbers = [1, 2, 3, 4, 5]
# Sum of list
print("Sum of numbers:", sum(numbers))
# Add 6 and remove 2
numbers.append(6)
numbers.remove(2)
print("Updated list:", numbers)
# Slice first 3 elements
print("First 3 elements:", numbers[:3])

# ---------------------------
# Exercise 2: Tuples
# ---------------------------
fruits = ("apple", "banana", "cherry")
# Access third element
print("Third fruit:", fruits[2])
# Slice last 2 elements
print("Last 2 fruits:", fruits[-2:])
# Combine with another tuple
more_fruits = ("orange", "kiwi")
combined = fruits + more_fruits
print("Combined tuple:", combined)

# ---------------------------
# Exercise 3: Sets
# ---------------------------
nums_set = {1, 2, 3, 4, 5}
# Add 6
nums_set.add(6)
# Remove 2
nums_set.remove(2)
print("Updated set:", nums_set)
# Union and intersection
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)

# ---------------------------
# Exercise 4: Dictionaries
# ---------------------------
student = {"name": "Fatima", "age": 21}
# Add new key
student["major"] = "CS"
# Update age
student["age"] = 22
# Remove key
student.pop("major")
print("Updated dictionary:", student)
# Access with get()
print("Name:", student.get("name"))
