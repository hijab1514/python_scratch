"""
Local and Global Variables in Python
------------------------------------
Variables defined inside a function are local.
Variables defined outside a function are global.
"""

# Global variable
x = 10

def local_example():
    # Local variable
    y = 5
    print("Inside function, x:", x)  # Access global
    print("Inside function, y:", y)

local_example()
# print(y)  # ❌ Error: y is local

# Modifying global variable inside function
def modify_global():
    global x
    x += 5

print("Before modify_global:", x)
modify_global()
print("After modify_global:", x)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a local variable inside a function and try to access it outside.
# 2. Modify a global variable using 'global' keyword.
# 3. Observe what happens if you assign a value to a global variable without 'global'.
