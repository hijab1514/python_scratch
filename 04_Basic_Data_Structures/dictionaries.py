"""
Dictionaries in Python
---------------------
Unordered, mutable collections of key-value pairs. Keys must be unique.
"""

# Creating dictionaries
student = {"name": "Fatima", "age": 21, "major": "CS"}
scores = {"Math": 95, "Physics": 90}

print("Student dictionary:", student)
print("Scores dictionary:", scores)

# Accessing values
print("Student name:", student["name"])
print("Math score:", scores.get("Math"))

# Adding or updating values
student["age"] = 22
student["year"] = "Senior"
print("Updated student:", student)

# Removing items
student.pop("year")
print("After pop:", student)
del student["age"]
print("After del:", student)

# Dictionary operations
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a dictionary with 3 key-value pairs and print all keys.
# 2. Add a new key-value pair and update an existing one.
# 3. Remove a key using pop() and del.
# 4. Use get() to safely access a value.
