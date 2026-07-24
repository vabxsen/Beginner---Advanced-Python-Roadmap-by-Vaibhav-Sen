"""
=========================================================
Topic : Lambda Functions in Python
=========================================================

This program demonstrates:
1. What are Lambda Functions?
2. Lambda with One Argument
3. Lambda with Multiple Arguments
4. Lambda with map()
5. Lambda with filter()
6. Lambda with reduce()
7. Lambda with sorted()
8. Practical Examples
"""

from functools import reduce

print("=" * 60)
print("LAMBDA FUNCTIONS IN PYTHON")
print("=" * 60)

# =======================================================
# BASIC LAMBDA FUNCTION
# =======================================================

print("\n1. Basic Lambda Function")

square = lambda x: x * x

print("Square of 5:", square(5))
print("Square of 10:", square(10))

# =======================================================
# MULTIPLE ARGUMENTS
# =======================================================

print("\n2. Lambda with Multiple Arguments")

add = lambda a, b: a + b
multiply = lambda a, b: a * b

print("Addition:", add(15, 20))
print("Multiplication:", multiply(6, 8))

# =======================================================
# LAMBDA WITH CONDITIONAL EXPRESSION
# =======================================================

print("\n3. Lambda with if-else")

even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

print("25 is", even_or_odd(25))
print("100 is", even_or_odd(100))

# =======================================================
# LAMBDA WITH map()
# =======================================================

print("\n4. map() Function")

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Original:", numbers)
print("Squares :", squares)

# =======================================================
# LAMBDA WITH filter()
# =======================================================

print("\n5. filter() Function")

numbers = [12, 5, 8, 20, 33, 42, 15]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Numbers :", numbers)
print("Even Numbers :", even_numbers)

# =======================================================
# LAMBDA WITH reduce()
# =======================================================

print("\n6. reduce() Function")

numbers = [10, 20, 30, 40]

total = reduce(lambda x, y: x + y, numbers)

print("Numbers :", numbers)
print("Total :", total)

# =======================================================
# LAMBDA WITH sorted()
# =======================================================

print("\n7. sorted() Function")

students = [
    ("Alice", 90),
    ("Bob", 82),
    ("Charlie", 95),
    ("David", 78)
]

sorted_students = sorted(students, key=lambda student: student[1])

print("Sorted by Marks:")

for student in sorted_students:
    print(student)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n8. Sort Dictionary by Value")

products = {
    "Laptop": 80000,
    "Keyboard": 3000,
    "Mouse": 1500,
    "Monitor": 18000
}

sorted_products = sorted(products.items(),
                         key=lambda item: item[1])

for item in sorted_products:
    print(item)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n9. Convert Names to Uppercase")

names = ["alice", "bob", "charlie", "david"]

uppercase_names = list(map(lambda name: name.upper(), names))

print(uppercase_names)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n10. Filter Adult Ages")

ages = [12, 18, 25, 15, 40, 17, 21]

adults = list(filter(lambda age: age >= 18, ages))

print("Adults:", adults)

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n11. Find Maximum Number")

numbers = [45, 89, 23, 100, 56]

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print("Maximum:", maximum)

# =======================================================
# PRACTICAL EXAMPLE 5
# =======================================================

print("\n12. Calculate Student Grades")

marks = [78, 85, 92, 64, 99]

grades = list(map(
    lambda mark: "Pass" if mark >= 40 else "Fail",
    marks
))

for mark, grade in zip(marks, grades):
    print(f"{mark} -> {grade}")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Lambda creates anonymous functions.")
print("2. Lambda functions contain only one expression.")
print("3. map() transforms data.")
print("4. filter() selects matching elements.")
print("5. reduce() combines elements into one value.")
print("6. sorted() can use lambda as a key.")
print("7. Lambdas make code concise.")
print("8. Best for short, simple operations.")
print("9. Avoid complex logic inside lambda.")
print("10. Commonly used in data processing.")

print("\nEnd of Program")