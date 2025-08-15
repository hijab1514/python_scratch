"""
Loops in Python
---------------
Used to execute a block of code repeatedly.
"""

# For loop - iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# For loop with range
for i in range(5):
    print("i:", i)

# While loop
count = 0
while count < 5:
    print("count:", count)
    count += 1

# break statement
for i in range(10):
    if i == 3:
        print("Breaking loop at i =", i)
        break
    print(i)

# continue statement
for i in range(5):
    if i == 2:
        print("Skipping i =", i)
        continue
    print(i)

# pass statement
for i in range(3):
    if i == 1:
        pass  # placeholder, does nothing
    print("i:", i)

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Print numbers from 1 to 50 using a loop.
# 2. Print all even numbers between 1 and 100.
# 3. Use break to stop a loop when a condition is met.
# 4. Use continue to skip printing multiples of 5.
# 5. Create a simple multiplication table using nested loops.
