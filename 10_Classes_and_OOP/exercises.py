"""
Practice Exercises - Classes and OOP
------------------------------------
Solve these exercises to practice OOP concepts: classes, inheritance, polymorphism, and encapsulation.
"""

# ---------------------------
# Exercise 1: Classes and Objects
# ---------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display()
car2.display()

# ---------------------------
# Exercise 2: Inheritance
# ---------------------------
class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    def start(self):
        print("Bike started with kick")

bike = Bike()
bike.start()

# ---------------------------
# Exercise 3: Polymorphism
# ---------------------------
class Bird:
    def action(self):
        print("Bird flies")

class Dog:
    def action(self):
        print("Dog runs")

animals = [Bird(), Dog()]

for a in animals:
    a.action()

# ---------------------------
# Exercise 4: Encapsulation
# ---------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s1 = Student("Fatima", 90)
print("Marks:", s1.get_marks())
s1.set_marks(95)
print("Updated marks:", s1.get_marks())
# print(s1.__marks)  # ❌ Error: private variable
