"""
Practice Exercises - Control Structures
---------------------------------------
Solve these exercises to practice if-else statements and loops.
"""

# ---------------------------
# Exercise 1: Conditional Statements
# ---------------------------
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Check divisibility
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")

# ---------------------------
# Exercise 2: Loops
# ---------------------------
# Print numbers from 1 to 20
for i in range(1, 21):
    print(i, end=" ")
print()

# Print all even numbers from 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Loop with break
for i in range(10):
    if i == 6:
        print("Stopping at 6")
        break
    print(i, end=" ")
print()

# Loop with continue
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# Nested loop example: multiplication table for 1-3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()
