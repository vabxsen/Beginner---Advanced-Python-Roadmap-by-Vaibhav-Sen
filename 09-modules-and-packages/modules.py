"""
=========================================================
Topic : Modules in Python
=========================================================

This program demonstrates:
1. What are Modules?
2. Importing Modules
3. Importing Specific Functions
4. Using Aliases
5. Built-in Modules
6. Creating User-Defined Modules
7. dir() Function
8. __name__ Variable
9. Practical Examples
"""

print("=" * 60)
print("MODULES IN PYTHON")
print("=" * 60)

# =======================================================
# IMPORTING A MODULE
# =======================================================

import math

print("\n1. Importing a Module")

print("Square Root of 64 :", math.sqrt(64))
print("Value of PI       :", math.pi)
print("Power (2^5)       :", math.pow(2, 5))

# =======================================================
# IMPORTING SPECIFIC FUNCTIONS
# =======================================================

from math import factorial, ceil, floor

print("\n2. Importing Specific Functions")

print("Factorial of 5 :", factorial(5))
print("Ceil of 7.2    :", ceil(7.2))
print("Floor of 7.8   :", floor(7.8))

# =======================================================
# USING ALIAS
# =======================================================

import random as rd

print("\n3. Module Alias")

print("Random Number :", rd.randint(1, 100))
print("Random Choice :", rd.choice(["Apple", "Banana", "Mango"]))

# =======================================================
# DATETIME MODULE
# =======================================================

import datetime

print("\n4. Datetime Module")

today = datetime.datetime.now()

print("Current Date & Time :", today)
print("Current Year        :", today.year)
print("Current Month       :", today.month)
print("Current Day         :", today.day)

# =======================================================
# OS MODULE
# =======================================================

import os

print("\n5. OS Module")

print("Current Working Directory:")
print(os.getcwd())

# =======================================================
# PLATFORM MODULE
# =======================================================

import platform

print("\n6. Platform Module")

print("Operating System :", platform.system())
print("Processor        :", platform.processor())
print("Python Version   :", platform.python_version())

# =======================================================
# DIR() FUNCTION
# =======================================================

print("\n7. dir() Function")

print("Some functions available in math module:")
print(dir(math)[:15])      # Display first 15 members

# =======================================================
# __name__ VARIABLE
# =======================================================

print("\n8. __name__ Variable")

print("Current Module Name :", __name__)

# =======================================================
# USER-DEFINED MODULE (Example)
# =======================================================

print("\n9. User-Defined Module")

print("""
Suppose you have another file named calculator.py

# calculator.py
--------------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
--------------------------

You can import it like this:

import calculator

print(calculator.add(5, 3))
""")

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n10. Random Password Generator")

import string

characters = string.ascii_letters + string.digits

password = ""

for i in range(10):
    password += rd.choice(characters)

print("Generated Password :", password)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n11. Random Dice Roll")

dice = rd.randint(1, 6)

print("Dice Number :", dice)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n12. Area of Circle")

radius = 7

area = math.pi * radius ** 2

print("Radius :", radius)
print("Area   :", round(area, 2))

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n13. Date Formatting")

formatted_date = today.strftime("%d-%m-%Y")

print("Formatted Date :", formatted_date)

# =======================================================
# PRACTICAL EXAMPLE 5
# =======================================================

print("\n14. Countdown")

import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Time's Up!")

# =======================================================
# COMMON BUILT-IN MODULES
# =======================================================

print("\n15. Popular Built-in Modules")

modules = [
    "math",
    "random",
    "datetime",
    "time",
    "os",
    "platform",
    "string",
    "sys",
    "statistics",
    "collections"
]

for module in modules:
    print(module)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Modules help organize Python code.")
print("2. import imports an entire module.")
print("3. from module import function imports specific functions.")
print("4. as creates an alias for a module.")
print("5. Built-in modules provide ready-made functionality.")
print("6. User-defined modules improve code reusability.")
print("7. dir() lists module members.")
print("8. __name__ identifies the current module.")
print("9. Modules make programs modular and maintainable.")
print("10. Python provides hundreds of built-in modules.")

print("\nEnd of Program")