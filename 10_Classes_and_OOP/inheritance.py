"""
Inheritance in Python
--------------------
A class can inherit attributes and methods from another class.
"""

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Child class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Testing inheritance
dog = Dog("Buddy")
cat = Cat("Kitty")

dog.speak()
cat.speak()

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a parent class Vehicle with method start().
# 2. Create a child class Car and override start() method.
# 3. Create multiple objects and call the overridden methods.
