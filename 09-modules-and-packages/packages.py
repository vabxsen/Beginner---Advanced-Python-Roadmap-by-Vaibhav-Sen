"""
=========================================================
Topic : Packages in Python
=========================================================

This program demonstrates:
1. What are Packages?
2. Package Structure
3. Importing Packages
4. Importing Modules from Packages
5. Using Aliases
6. __init__.py
7. Built-in Packages
8. Installing External Packages
9. Practical Examples
"""
print("=" * 60)
print("PACKAGES IN PYTHON")
print("=" * 60)

# =======================================================
# WHAT IS A PACKAGE?
# =======================================================

print("\n1. What is a Package?")

print("""
A Package is a collection of related Python modules.

Example Structure:

my_package/
│
├── __init__.py
├── calculator.py
├── geometry.py
└── converter.py

Each .py file is called a Module.
The entire folder is called a Package.
""")

# =======================================================
# IMPORTING A PACKAGE
# =======================================================

print("\n2. Importing Modules from a Package")

print("""
Suppose we have:

my_package/
│
├── __init__.py
└── calculator.py

calculator.py

def add(a, b):
    return a + b

------------------------------

Import Example:

from my_package import calculator

print(calculator.add(10, 20))
""")

# =======================================================
# IMPORT SPECIFIC FUNCTION
# =======================================================

print("\n3. Import Specific Function")

print("""
from my_package.calculator import add

print(add(15, 10))
""")

# =======================================================
# USING ALIAS
# =======================================================

print("\n4. Using Alias")

print("""
import math as m

print(m.sqrt(81))
print(m.pi)
""")

# =======================================================
# __init__.py
# =======================================================

print("\n5. __init__.py")

print("""
__init__.py tells Python that the folder
should be treated as a package.

It can also contain initialization code.

Example:

# __init__.py

print("Package Loaded")
""")

# =======================================================
# BUILT-IN PACKAGES
# =======================================================

print("\n6. Built-in Packages")

import math
import random
import statistics

numbers = [10, 20, 30, 40, 50]

print("Square Root :", math.sqrt(64))
print("Random Number :", random.randint(1, 100))
print("Average :", statistics.mean(numbers))

# =======================================================
# EXTERNAL PACKAGES
# =======================================================

print("\n7. External Packages")

print("""
External packages are installed using pip.

Examples:

pip install numpy
pip install pandas
pip install matplotlib
pip install requests
pip install flask
pip install django
pip install pillow
""")

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n8. Math Package Example")

radius = 10

area = math.pi * radius ** 2

print("Radius :", radius)
print("Area :", round(area, 2))

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n9. Random Password Generator")

import string

characters = string.ascii_letters + string.digits

password = ""

for i in range(8):
    password += random.choice(characters)

print("Password :", password)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n10. Statistics Package")

marks = [80, 92, 75, 88, 91, 95]

print("Marks :", marks)
print("Mean :", statistics.mean(marks))
print("Median :", statistics.median(marks))
print("Highest :", max(marks))
print("Lowest :", min(marks))

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n11. Simulating Dice Roll")

dice = random.randint(1, 6)

print("Dice Number :", dice)

# =======================================================
# PACKAGE HIERARCHY
# =======================================================

print("\n12. Example Package Hierarchy")

print("""
project/

│
├── main.py
│
├── utilities/
│   ├── __init__.py
│   ├── calculator.py
│   ├── converter.py
│   └── validator.py
│
├── database/
│   ├── __init__.py
│   ├── mysql.py
│   └── sqlite.py
│
└── models/
    ├── __init__.py
    ├── student.py
    └── employee.py
""")

# =======================================================
# BENEFITS OF PACKAGES
# =======================================================

print("\n13. Benefits of Packages")

benefits = [
    "Organized Code",
    "Easy Maintenance",
    "Reusable Modules",
    "Avoid Name Conflicts",
    "Better Project Structure",
    "Improved Readability",
    "Easy Distribution"
]

for index, benefit in enumerate(benefits, start=1):
    print(f"{index}. {benefit}")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. A package is a collection of related modules.")
print("2. Modules are individual .py files.")
print("3. __init__.py marks a directory as a package.")
print("4. Packages improve project organization.")
print("5. Use 'import' and 'from' to import packages.")
print("6. Aliases make module names shorter.")
print("7. pip installs external packages.")
print("8. Built-in packages come with Python.")
print("9. Packages make applications scalable.")
print("10. Professional Python projects heavily use packages.")

print("\nEnd of Program")