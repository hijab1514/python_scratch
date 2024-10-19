# Python Variables, Lists, Tuples, and Dictionaries

## 1. Variables
A variable in Python is used to store a value.

```python
name = "John Doe"
age = 25
height = 5.9

Common Functions for Variables:
type(): Returns the type of the variable.
str(): Converts a value to a string.
int(): Converts a value to an integer.
float(): Converts a value to a float.
  
  print(type(name))  # Output: <class 'str'>
print(int(height))  # Output: 5



  #Dictionaries (Maps)
  A map, or dictionary, is a collection of key-value pairs. Unlike lists or tuples, dictionaries use keys to access values rather than numeric indices. Dictionaries are mutab
  # Dictionary declaration
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

# Accessing values
print("Student Name:", student["name"])
print("Student Major:", student["major"])

# Modifying values
student["age"] = 23
print("Updated Age:", student["age"])

# Adding new key-value pairs
student["GPA"] = 3.9
print("Student Dictionary after adding GPA:", student)

# Removing key-value pairs
del student["major"]
print("After removing 'major':", student)


  # Accessing keys, values, and items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Get value of a key
print("Name:", student.get("name"))
print("GPA:", student.get("GPA", "Not Available"))  # 'GPA' key does not exist

# Update the dictionary
student.update({"GPA": 3.9, "age": 23})
print("Updated student dictionary:", student)

# Pop a key-value pair
age = student.pop("age")
print("Popped age:", age)
print("Student dictionary after pop:", student)

# Pop the last inserted key-value pair
last_item = student.popitem()
print("Last item popped:", last_item)
print("Student dictionary after popitem:", student)

# Length of dictionary
print("Number of items in the dictionary:", len(student))

  
