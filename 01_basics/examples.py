# ==============================
# Python Basics Examples
# ==============================

# 1. Hello World
print("Hello, Python!")  # Prints a simple message

# 2. Variables
name = "Fatima"       # String variable
age = 20              # Integer variable
height = 5.5          # Float variable
is_student = True     # Boolean variable

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 3. Comments
# This is a single-line comment

"""
This is a
multi-line comment
"""

# 4. Printing Variables with f-strings
print(f"My name is {name} and I am {age} years old.")

# 5. Taking User Input
# Uncomment the following lines to test input
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# 6. Basic Math Operations
a = 10
b = 5

print("\nBasic Math Operations:")
print("Addition:", a + b)          # 15
print("Subtraction:", a - b)       # 5
print("Multiplication:", a * b)    # 50
print("Division:", a / b)          # 2.0
print("Floor Division:", a // b)   # 2
print("Modulo:", a % b)            # 0
print("Power:", a ** b)            # 100000

# 7. Data Types Examples
print("\nData Types Examples:")
my_int = 10
my_float = 3.14
my_str = "Python"
my_bool = True
my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7)
my_dict = {"name": "Fatima", "age": 20}
my_set = {1, 2, 3, 2, 1}  # duplicates removed automatically

print("Integer:", my_int)
print("Float:", my_float)
print("String:", my_str)
print("Boolean:", my_bool)
print("List:", my_list)
print("Tuple:", my_tuple)
print("Dictionary:", my_dict)
print("Set:", my_set)

# 8. Combining Input, Variables, and Math
# Uncomment to test
# length = float(input("Enter length of rectangle: "))
# width = float(input("Enter width of rectangle: "))
# area = length * width
# print(f"Area of rectangle: {area}")

# 9. Example: Using multiple variables
first_name = "Fatima"
last_name = "Hijab"
full_name = first_name + " " + last_name
print("\nFull Name:", full_name)

# 10. Logical Operations
x = True
y = False
print("\nLogical Operations:")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# 11. If-Else Mini Example
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 12. Loops Mini Example
print("\nFor Loop Example:")
for i in range(5):
    print(i, end=" ")  # Prints: 0 1 2 3 4

print("\n\nWhile Loop Example:")
i = 0
while i < 5:
    print(i, end=" ")  # Prints: 0 1 2 3 4
    i += 1

print("\n\nEnd of Python Basics Examples")
