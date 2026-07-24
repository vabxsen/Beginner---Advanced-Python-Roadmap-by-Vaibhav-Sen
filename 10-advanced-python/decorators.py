"""
=========================================================
Topic : Decorators in Python
=========================================================

This program demonstrates:
1. Basic Decorators
2. Functions as Objects
3. Nested Functions
4. Decorator Functions
5. @ Decorator Syntax
6. Decorators with Arguments
7. Multiple Decorators
8. Built-in Decorators
9. Practical Examples
"""

import time
from functools import wraps

print("=" * 60)
print("DECORATORS IN PYTHON")
print("=" * 60)

# =======================================================
# FUNCTIONS ARE OBJECTS
# =======================================================

print("\n1. Functions are Objects")

def greet():
    print("Hello, Python!")

message = greet
message()

# =======================================================
# NESTED FUNCTIONS
# =======================================================

print("\n2. Nested Functions")

def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()

# =======================================================
# BASIC DECORATOR
# =======================================================

def decorator(function):

    def wrapper():
        print("Before Function Execution")
        function()
        print("After Function Execution")

    return wrapper

@decorator
def welcome():
    print("Welcome to Python!")

print("\n3. Basic Decorator")

welcome()

# =======================================================
# DECORATOR WITH ARGUMENTS
# =======================================================

def smart_divide(function):

    def wrapper(a, b):

        if b == 0:
            print("Cannot Divide by Zero")
            return

        return function(a, b)

    return wrapper

@smart_divide
def divide(a, b):
    print("Result:", a / b)

print("\n4. Decorator with Arguments")

divide(20, 5)
divide(20, 0)

# =======================================================
# MULTIPLE DECORATORS
# =======================================================

def uppercase(function):

    def wrapper():
        return function().upper()

    return wrapper

def add_stars(function):

    def wrapper():
        return "***** " + function() + " *****"

    return wrapper

@add_stars
@uppercase
def language():
    return "python"

print("\n5. Multiple Decorators")

print(language())

# =======================================================
# BUILT-IN DECORATORS
# =======================================================

class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

print("\n6. @property Decorator")

student = Student(95)

print("Marks:", student.marks)

# =======================================================
# TIMING DECORATOR
# =======================================================

def timer(function):

    @wraps(function)
    def wrapper():

        start = time.time()

        function()

        end = time.time()

        print(f"Execution Time: {end-start:.5f} seconds")

    return wrapper

@timer
def calculation():

    total = 0

    for i in range(100000):
        total += i

print("\n7. Timer Decorator")

calculation()

# =======================================================
# LOGIN DECORATOR
# =======================================================

logged_in = True

def login_required(function):

    def wrapper():

        if logged_in:
            function()
        else:
            print("Please Login First!")

    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

print("\n8. Login Decorator")

dashboard()

# =======================================================
# LOGGING DECORATOR
# =======================================================

def logger(function):

    def wrapper():
        print(f"Executing Function: {function.__name__}")
        function()
        print("Execution Completed")

    return wrapper

@logger
def display():
    print("Learning Decorators")

print("\n9. Logging Decorator")

display()

# =======================================================
# PRACTICAL EXAMPLE
# =======================================================

def repeat(function):

    def wrapper():

        for i in range(3):
            function()

    return wrapper

@repeat
def hello():
    print("Hello World!")

print("\n10. Repeat Decorator")

hello()

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Decorators modify function behavior.")
print("2. Functions are first-class objects.")
print("3. Decorators return wrapper functions.")
print("4. @ syntax applies decorators easily.")
print("5. Decorators can accept arguments.")
print("6. Multiple decorators can be stacked.")
print("7. @property is a built-in decorator.")
print("8. @wraps preserves original function metadata.")
print("9. Decorators improve code reusability.")
print("10. Common uses: logging, authentication, timing, caching.")

print("\nEnd of Program")