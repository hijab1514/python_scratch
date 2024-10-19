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

  # Common Methods/Functions:
# len(): Returns the number of elements in a tuple.
# count(): Counts the number of occurrences of a specified element.
# index(): Returns the index of the first occurrence of a specified element.
 # Example of Common Methods:

  # Length of the tuple
print("Number of elements:", len(coordinates))  # Output: 3

# Count occurrences
banana_count = coordinates.count(10)
print("Count of 10 in coordinates:", banana_count)  # Output: 1

# Index of an element
banana_index = coordinates.index(20)
print("First occurrence of 20 at index:", banana_index)  # Output: 1
