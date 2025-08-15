"""
Polymorphism in Python
---------------------
Objects of different classes can be treated similarly if they have same methods.
"""

class Bird:
    def speak(self):
        print("Chirp chirp")

class Dog:
    def speak(self):
        print("Bark bark")

class Cat:
    def speak(self):
        print("Meow meow")

# Polymorphism example
animals = [Bird(), Dog(), Cat()]

for animal in animals:
    animal.speak()  # Same method name, different implementation

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create two classes with a method called action().
# 2. Store objects of both classes in a list.
# 3. Call action() on each object to demonstrate polymorphism.
