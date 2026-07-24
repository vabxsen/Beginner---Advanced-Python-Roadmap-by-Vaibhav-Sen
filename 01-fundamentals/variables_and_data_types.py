"""
=========================================================
Topic : Variables and Data Types in Python
=========================================================

This program demonstrates:
1. Variables
2. Naming conventions
3. Multiple assignment
4. Dynamic typing
5. Basic data types
6. Type checking
7. Type conversion
8. Identity (id)
9. Constants (by convention)
10. Printing formatted output
"""
# =======================================================
# VARIABLES
# =======================================================

name = "Alice"
age = 25
height = 5.6
is_student = True

print("----- Basic Variables -----")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

print()

# =======================================================
# MULTIPLE VARIABLE ASSIGNMENT
# =======================================================

x, y, z = 10, 20, 30

print("----- Multiple Assignment -----")
print("x =", x)
print("y =", y)
print("z =", z)

print()

# =======================================================
# DYNAMIC TYPING
# =======================================================

value = 100
print("Value:", value, "| Type:", type(value))

value = "Now I'm a string"
print("Value:", value, "| Type:", type(value))

print()

# =======================================================
# BASIC DATA TYPES
# =======================================================

integer_number = 50
floating_number = 12.75
complex_number = 4 + 7j
text = "Python"
boolean_value = False

print("----- Data Types -----")
print(type(integer_number))
print(type(floating_number))
print(type(complex_number))
print(type(text))
print(type(boolean_value))

print()

# =======================================================
# TYPE CONVERSION
# =======================================================

number_string = "150"

converted_integer = int(number_string)
converted_float = float(number_string)
converted_string = str(converted_integer)

print("----- Type Conversion -----")
print(converted_integer)
print(converted_float)
print(converted_string)

print()

# =======================================================
# CONSTANTS (Naming Convention)
# =======================================================

PI = 3.14159
MAX_USERS = 100

print("PI =", PI)
print("Maximum Users =", MAX_USERS)

print()

# =======================================================
# VARIABLE IDENTITY
# =======================================================

a = 10
b = a

print("----- Memory Identity -----")
print("a =", a, "ID:", id(a))
print("b =", b, "ID:", id(b))

print()

# =======================================================
# FORMATTED STRINGS (f-strings)
# =======================================================

language = "Python"
version = 3.14

print("----- Formatted Output -----")
print(f"I am learning {language} version {version}")

print()

# =======================================================
# CHECKING VARIABLE TYPES
# =======================================================

print("----- isinstance() Examples -----")
print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(height, float))
print(isinstance(is_student, bool))

print()

# =======================================================
# SUMMARY
# =======================================================

print("Variables allow storing data.")
print("Python is dynamically typed.")
print("Different data types are used for different purposes.")
print("Type conversion helps convert data between formats.")