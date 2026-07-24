"""
=========================================================
Topic : Functions in Python
=========================================================

This program demonstrates:
1. Creating Functions
2. Calling Functions
3. Parameters & Arguments
4. Default Arguments
5. Keyword Arguments
6. Variable-Length Arguments (*args, **kwargs)
7. Return Statement
8. Local & Global Variables
9. Recursive Functions
10. Lambda Functions
"""
print("=" * 60)
print("FUNCTIONS IN PYTHON")
print("=" * 60)

# =======================================================
# SIMPLE FUNCTION
# =======================================================

def greet():
    print("Hello! Welcome to Python Functions.")

print("\n1. Simple Function")
greet()

# =======================================================
# FUNCTION WITH PARAMETERS
# =======================================================

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

print("\n2. Function with Parameters")
introduce("Alice", 21)
introduce("Bob", 25)

# =======================================================
# FUNCTION WITH RETURN VALUE
# =======================================================

def add(a, b):
    return a + b

print("\n3. Return Statement")
result = add(15, 10)
print("Addition =", result)

# =======================================================
# DEFAULT ARGUMENTS
# =======================================================

def country(name, nation="India"):
    print(f"{name} lives in {nation}.")

print("\n4. Default Arguments")
country("Cheese")
country("John", "USA")

# =======================================================
# KEYWORD ARGUMENTS
# =======================================================

def student(name, course, semester):
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Semester: {semester}")

print("\n5. Keyword Arguments")
student(course="B.Tech", semester=5, name="Vaibhav")

# =======================================================
# VARIABLE LENGTH ARGUMENTS (*args)
# =======================================================

def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

print("\n6. *args Example")
total_marks(80, 75, 90, 95)

# =======================================================
# VARIABLE LENGTH KEYWORD ARGUMENTS (**kwargs)
# =======================================================

def employee(**details):
    print("\nEmployee Details:")
    for key, value in details.items():
        print(f"{key} : {value}")

print("\n7. **kwargs Example")
employee(name="Alice", age=24, department="IT", salary=50000)

# =======================================================
# LOCAL AND GLOBAL VARIABLES
# =======================================================

company = "OpenAI"      # Global Variable

def show_company():
    department = "Research"   # Local Variable
    print("Company:", company)
    print("Department:", department)

print("\n8. Local & Global Variables")
show_company()

# =======================================================
# RECURSIVE FUNCTION
# =======================================================

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("\n9. Recursive Function")
print("Factorial of 5 =", factorial(5))

# =======================================================
# LAMBDA FUNCTION
# =======================================================

square = lambda x: x * x

print("\n10. Lambda Function")
print("Square of 9 =", square(9))

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

def calculate_area(length, width):
    area = length * width
    return area

print("\n11. Area of Rectangle")
print("Area =", calculate_area(15, 8))

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print("\n12. Even or Odd")
print("27 is", even_or_odd(27))
print("100 is", even_or_odd(100))

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

def maximum(a, b, c):
    return max(a, b, c)

print("\n13. Largest Number")
print("Largest =", maximum(45, 89, 67))

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

def calculate_percentage(obtained, total):
    return (obtained / total) * 100

percentage = calculate_percentage(445, 500)

print("\n14. Percentage Calculator")
print(f"Percentage = {percentage:.2f}%")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. def           -> Defines a function")
print("2. Parameters    -> Variables in function definition")
print("3. Arguments     -> Values passed to function")
print("4. return        -> Sends value back to caller")
print("5. Default Args  -> Optional parameter values")
print("6. *args         -> Multiple positional arguments")
print("7. **kwargs      -> Multiple keyword arguments")
print("8. Scope         -> Local and Global variables")
print("9. Recursion     -> Function calling itself")
print("10. Lambda       -> Anonymous one-line function")

print("\nEnd of Program")