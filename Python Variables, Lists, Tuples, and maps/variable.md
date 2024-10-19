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

    ## 2. lists
     list is a mutable (changeable) collection of elements. You can store multiple items in a list, which can contain elements of different data types.
    # List declaration
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements
print("First fruit:", fruits[0])   # Accessing the first element
print("Last fruit:", fruits[-1])   # Accessing the last element

# Modifying elements
fruits[1] = "blueberry"
print("Modified List:", fruits)

# Adding elements
fruits.append("elderberry")
print("After adding a new fruit:", fruits)

# Removing elements
fruits.remove("cherry")
print("After removing an element:", fruits)
Common Methods for Lists:
append(): Adds an element to the end of the list.
extend(): Adds all elements of an iterable (like another list) to the end of the list.
insert(): Inserts an element at a specified index.
remove(): Removes the first occurrence of an element.
pop(): Removes and returns the element at the specified position (default is the last element).
sort(): Sorts the list in ascending order.
reverse(): Reverses the order of elements in the list.
  len(): Returns the number of elements in the list
  # Append
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Sort
fruits.sort()
print("After sorting:", fruits)  # Output: ['apple', 'banana', 'blueberry', 'date']

  # 3. Tuple
  A tuple is an immutable (unchangeable) collection of elements. Tuples are useful when you want to store multiple items and ensure they cannot be altered.

  # Tuple declaration
coordinates = (10, 20, 30)

# Accessing elements
print("First coordinate:", coordinates[0])
print("Second coordinate:", coordinates[1])

# Tuples are immutable, so you can't change their values
# The following line would throw an error if uncommented:
# coordinates[0] = 40  # This will raise a TypeError

# Tuple unpacking
x, y, z = coordinates
print(f"Unpacked coordinates: x={x}, y={y}, z={z}")

  Common Methods/Functions:
len(): Returns the number of elements in a tuple.
count(): Counts the number of occurrences of a specified element.
index(): Returns the index of the first occurrence of a specified element.
Example of Common Methods:

  # Length of the tuple
print("Number of elements:", len(coordinates))  # Output: 3

# Count occurrences
banana_count = coordinates.count(10)
print("Count of 10 in coordinates:", banana_count)  # Output: 1

# Index of an element
banana_index = coordinates.index(20)
print("First occurrence of 20 at index:", banana_index)  # Output: 1

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

  
