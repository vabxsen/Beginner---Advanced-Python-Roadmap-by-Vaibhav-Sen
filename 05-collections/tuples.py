"""
=========================================================
Topic : Tuples in Python
=========================================================

This program demonstrates:
1. Creating Tuples
2. Accessing Elements
3. Tuple Slicing
4. Tuple Packing
5. Tuple Unpacking
6. Tuple Methods
7. Nested Tuples
8. Iterating Through Tuples
9. Tuple Concatenation & Repetition
10. Practical Examples
"""

print("=" * 60)
print("TUPLES IN PYTHON")
print("=" * 60)

# =======================================================
# CREATING TUPLES
# =======================================================

numbers = (10, 20, 30, 40, 50)
fruits = ("Apple", "Banana", "Mango", "Orange")
mixed = (100, "Python", 3.14, True)

print("\n1. Creating Tuples")
print(numbers)
print(fruits)
print(mixed)

# =======================================================
# ACCESSING ELEMENTS
# =======================================================

print("\n2. Accessing Elements")

print("First Number :", numbers[0])
print("Last Number  :", numbers[-1])
print("Second Fruit :", fruits[1])

# =======================================================
# TUPLE SLICING
# =======================================================

print("\n3. Tuple Slicing")

print("First Three :", numbers[:3])
print("Last Two    :", numbers[-2:])
print("Middle      :", numbers[1:4])

# =======================================================
# IMMUTABILITY
# =======================================================

print("\n4. Tuple Immutability")

print("Tuples cannot be modified after creation.")

# Uncommenting the next line will raise an error.
# numbers[0] = 99

# =======================================================
# TUPLE PACKING
# =======================================================

print("\n5. Tuple Packing")

student = ("Alice", 20, "Computer Science")

print(student)

# =======================================================
# TUPLE UNPACKING
# =======================================================

print("\n6. Tuple Unpacking")

name, age, course = student

print("Name   :", name)
print("Age    :", age)
print("Course :", course)

# =======================================================
# TUPLE METHODS
# =======================================================

print("\n7. Tuple Methods")

values = (5, 8, 5, 10, 15, 5)

print("Tuple :", values)
print("Count of 5 :", values.count(5))
print("Index of 10:", values.index(10))
print("Length :", len(values))

# =======================================================
# ITERATING THROUGH TUPLES
# =======================================================

print("\n8. Loop Through Tuple")

for fruit in fruits:
    print(fruit)

# =======================================================
# NESTED TUPLES
# =======================================================

print("\n9. Nested Tuples")

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
)

for student in students:
    print(student)

# =======================================================
# CONCATENATION
# =======================================================

print("\n10. Tuple Concatenation")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print(combined)

# =======================================================
# REPETITION
# =======================================================

print("\n11. Tuple Repetition")

repeat = ("Python",) * 4

print(repeat)

# =======================================================
# MEMBERSHIP OPERATORS
# =======================================================

print("\n12. Membership Operators")

print("20 in numbers :", 20 in numbers)
print("100 in numbers:", 100 in numbers)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n13. Student Record")

student = ("Vaibhav", 21, "B.Tech CSD", 8.7)

print("Name :", student[0])
print("Age  :", student[1])
print("Course:", student[2])
print("CGPA :", student[3])

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n14. Swapping Variables")

a = 100
b = 200

print("Before Swap:", a, b)

a, b = b, a

print("After Swap :", a, b)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n15. Maximum and Minimum")

marks = (85, 91, 67, 98, 74)

print("Marks :", marks)
print("Highest :", max(marks))
print("Lowest  :", min(marks))
print("Total   :", sum(marks))

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Tuples are ordered collections.")
print("2. Tuples are immutable (cannot be modified).")
print("3. Tuples allow duplicate values.")
print("4. Tuples support indexing and slicing.")
print("5. Packing stores multiple values together.")
print("6. Unpacking extracts values into variables.")
print("7. count() counts occurrences.")
print("8. index() returns the first matching index.")
print("9. Tuples are faster than lists for fixed data.")
print("10. Common uses: coordinates, records, database rows.")

print("\nEnd of Program")