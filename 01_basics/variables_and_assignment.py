"""
Variables and Assignment in Python
---------------------------------
Variables are used to store data that can be referenced and manipulated.
Python uses dynamic typing, so you don't need to declare variable types explicitly.
"""

# ---------------------------
# Variable Assignment
# ---------------------------
# Single assignment
x = 10
y = 3.14
name = "Fatima"
is_active = True

print("Single Assignment:")
print("x =", x)
print("y =", y)
print("name =", name)
print("is_active =", is_active)
print()

# Multiple assignment
a, b, c = 1, 2.5, "Hello"
print("Multiple Assignment:")
print("a =", a, "b =", b, "c =", c)
print()

# Assigning the same value to multiple variables
m = n = o = 100
print("Assigning Same Value:")
print("m =", m, "n =", n, "o =", o)
print()

# Swapping variables
x, y = y, x
print("After Swapping:")
print("x =", x)
print("y =", y)
print()

# ---------------------------
# Variable Naming Rules
# ---------------------------
# 1. Can contain letters, numbers, and underscores (_)
# 2. Cannot start with a number
# 3. Cannot use Python reserved keywords
# 4. Case-sensitive

# Examples
my_var = 5
_my_var2 = 10
# 2my_var = 15  # ❌ Invalid
# print = 20    # ❌ Avoid overwriting built-in functions

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create 3 variables: one integer, one float, and one string.
# 2. Assign the same value to 2 variables in a single line.
# 3. Swap the values of two variables and print the result.
# 4. Try creating a variable that starts with a number and observe the error.
# 5. Try overwriting a built-in function (like 'len') and see what happens.

