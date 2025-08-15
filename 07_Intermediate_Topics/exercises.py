
"""
Practice Exercises - Intermediate Topics
----------------------------------------
Solve these exercises to practice list comprehensions, lambda functions,
*args/**kwargs, decorators, and generators.
"""

# ---------------------------
# Exercise 1: List Comprehensions
# ---------------------------
squares = [x**2 for x in range(1, 11)]
print("Squares 1-10:", squares)

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# ---------------------------
# Exercise 2: Lambda Functions
# ---------------------------
cube = lambda x: x**3
print("Cube of 4:", cube(4))

# ---------------------------
# Exercise 3: *args and **kwargs
# ---------------------------
def sum_all(*args):
    return sum(args)

print("Sum of 1,2,3,4:", sum_all(1,2,3,4))

def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_info(name="Fatima", age=21)

# ---------------------------
# Exercise 4: Decorators
# ---------------------------
def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()

# ---------------------------
# Exercise 5: Generators
# ---------------------------
def even_gen(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

for val in even_gen(10):
    print("Even value:", val)
