  ## 2. lists
     list is a mutable (changeable) collection of elements. You can store multiple items in a list, which can contain elements of different data types.
    # List declaration
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements
`print("First fruit:", fruits[0])`   # Accessing the first element
print("Last fruit:", fruits[-1])   # Accessing the last element

# Modifying elements
```
fruits[1] = "blueberry"
print("Modified List:", fruits)
```

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
