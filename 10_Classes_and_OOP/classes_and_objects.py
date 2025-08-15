"""
Classes and Objects in Python
-----------------------------
Object-Oriented Programming (OOP) allows creating reusable objects.
"""

# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create objects
person1 = Person("Fatima", 21)
person2 = Person("Ali", 22)

# Access methods and attributes
person1.greet()
person2.greet()

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a class Car with attributes brand and model.
# 2. Define a method to display car details.
# 3. Create two objects and call the method for both.
