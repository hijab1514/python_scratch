# ==============================
# Python Basics Exercises
# ==============================

"""
Instructions:
- Try to solve each exercise.
- Write your solution in the space provided.
- Test your code by running this file.
"""

# ------------------------------
# Exercise 1: Hello World
# ------------------------------
# Print your name and hobby using the print() function
# Example Output: "Hello, my name is Fatima and I love painting"
print("\nExercise 1:")
# Write your code below
# print("Your solution here")


# ------------------------------
# Exercise 2: Variables
# ------------------------------
# Create variables for your name, age, and city
# Then print them in a single sentence using f-strings
print("\nExercise 2:")
# Example Output: "My name is Fatima, I am 20 years old and I live in Seoul."
# Write your code below
# name = ...
# age = ...
# city = ...
# print(f"...")

# ------------------------------
# Exercise 3: Data Types
# ------------------------------
# Create 3 variables of different data types: int, float, string
# Print the type of each variable using the type() function
print("\nExercise 3:")
# Example:
# number = 10
# price = 99.99
# name = "Fatima"
# print(type(number), type(price), type(name))
# Write your code below


# ------------------------------
# Exercise 4: Basic Math
# ------------------------------
# Ask the user to enter two numbers
# Calculate and print the sum, difference, product, division, floor division, modulo, and power
print("\nExercise 4:")
# Example:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Sum:", a+b)
# Write your code below


# ------------------------------
# Exercise 5: Input and Output
# ------------------------------
# Ask the user for their favorite color and print it
# Example Output: "Your favorite color is Blue"
print("\nExercise 5:")
# favorite_color = input("Enter your favorite color: ")
# print("Your favorite color is", favorite_color)


# ------------------------------
# Exercise 6: If-Else
# ------------------------------
# Ask the user for a number
# Check if it is even or odd
print("\nExercise 6:")
# number = int(input("Enter a number: "))
# Write your if-else statement below


# ------------------------------
# Exercise 7: Loops
# ------------------------------
# Print all even numbers between 1 and 20 using a for loop
print("\nExercise 7:")
# Write your code below


# ------------------------------
# Exercise 8: Combining Concepts
# ------------------------------
# Ask the user for the length and width of a rectangle
# Calculate the area and perimeter
print("\nExercise 8:")
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# area = ...
# perimeter = ...
# print(f"Area: {area}, Perimeter: {perimeter}")


# ------------------------------
# Exercise 9: Lists
# ------------------------------
# Create a list of 5 fruits and print the first and last fruit
print("\nExercise 9:")
# fruits = ["apple", "banana", "mango", "orange", "grape"]
# print(fruits[0], fruits[-1])


# ------------------------------
# Exercise 10: Mini Project
# ------------------------------
# Create a simple program that asks the user's name and age
# Then prints a message like:
# "Hello Fatima, you will be 25 years old next year"
print("\nExercise 10:")
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}, you will be {age+1} years old next year")

"""
Practice Exercises - Data Types and Variables
---------------------------------------------
Solve these exercises to practice Python basics.
"""

# ---------------------------
# Exercise 1: Variables and Assignment
# ---------------------------
# 1. Create 3 variables: one integer, one float, one string.
# 2. Print all variables in a single line.
int_var = 10
float_var = 3.14
str_var = "Python"
print(int_var, float_var, str_var)

# 3. Assign the same value (100) to 2 variables in a single line and print.
x = y = 100
print("x =", x, "y =", y)

# 4. Swap the values of two variables without using a third variable.
a, b = 5, 10
a, b = b, a
print("After swapping: a =", a, "b =", b)

# ---------------------------
# Exercise 2: Type Conversion
# ---------------------------
# 1. Convert float 12.75 to int and print.
f_num = 12.75
i_num = int(f_num)
print("Float to int:", i_num)

# 2. Convert integer 50 to float and string.
num = 50
print("Int to float:", float(num))
print("Int to string:", str(num))

# 3. Check boolean value of empty string and non-empty string.
empty_str = ""
non_empty_str = "Hello"
print("Empty string to bool:", bool(empty_str))
print("Non-empty string to bool:", bool(non_empty_str))

# 4. Perform an operation between int and string (will cause error),
# then convert string to int and try again.
num1 = 5
num2 = "10"
# print(num1 + num2)  # ❌ Uncomment to see TypeError
print("After converting string to int:", num1 + int(num2))

# ---------------------------
# Exercise 3: Extra Practice
# ---------------------------
# 1. Create variables with valid and invalid names and observe.
# 2. Try assigning None to a variable and print its type.
# 3. Experiment with dynamic typing by changing a variable type.
var = 100
print("Original type:", type(var))
var = "Now I'm a string"
print("After change:", type(var))

