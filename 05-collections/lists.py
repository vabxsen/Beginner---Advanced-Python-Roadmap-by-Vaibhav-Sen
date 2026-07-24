"""
=========================================================
Topic : Lists in Python
=========================================================

This program demonstrates:
1. Creating Lists
2. Accessing Elements
3. Slicing
4. Updating Elements
5. Adding Elements
6. Removing Elements
7. List Methods
8. Looping Through Lists
9. List Comprehension
10. Practical Examples
"""
print("=" * 60)
print("LISTS IN PYTHON")
print("=" * 60)

# =======================================================
# CREATING LISTS
# =======================================================

numbers = [10, 20, 30, 40, 50]
fruits = ["Apple", "Banana", "Mango", "Orange"]
mixed = [100, "Python", 3.14, True]

print("\n1. Creating Lists")
print(numbers)
print(fruits)
print(mixed)

# =======================================================
# ACCESSING ELEMENTS
# =======================================================

print("\n2. Accessing Elements")
print("First Fruit :", fruits[0])
print("Last Fruit  :", fruits[-1])
print("Third Number:", numbers[2])

# =======================================================
# LIST SLICING
# =======================================================

print("\n3. List Slicing")
print("First 3 Numbers :", numbers[:3])
print("Last 2 Numbers  :", numbers[-2:])
print("Middle Elements :", numbers[1:4])

# =======================================================
# UPDATING ELEMENTS
# =======================================================

print("\n4. Updating Elements")

fruits[1] = "Pineapple"
print(fruits)

# =======================================================
# ADDING ELEMENTS
# =======================================================

print("\n5. Adding Elements")

fruits.append("Kiwi")
fruits.insert(1, "Grapes")
fruits.extend(["Papaya", "Cherry"])

print(fruits)

# =======================================================
# REMOVING ELEMENTS
# =======================================================

print("\n6. Removing Elements")

fruits.remove("Kiwi")
fruits.pop()
del fruits[0]

print(fruits)

# =======================================================
# LIST METHODS
# =======================================================

print("\n7. List Methods")

marks = [90, 75, 82, 96, 65]

print("Original :", marks)

marks.sort()
print("Sorted :", marks)

marks.reverse()
print("Reversed :", marks)

print("Maximum :", max(marks))
print("Minimum :", min(marks))
print("Sum :", sum(marks))
print("Length :", len(marks))

# =======================================================
# LOOPING THROUGH A LIST
# =======================================================

print("\n8. Looping Through Lists")

for fruit in fruits:
    print(fruit)

# =======================================================
# LIST COMPREHENSION
# =======================================================

print("\n9. List Comprehension")

squares = [x ** 2 for x in range(1, 11)]
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Squares :", squares)
print("Even Numbers :", even_numbers)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n10. Student Marks")

student_marks = [78, 92, 85, 67, 95]

average = sum(student_marks) / len(student_marks)

print("Marks :", student_marks)
print("Average :", average)
print("Highest :", max(student_marks))
print("Lowest :", min(student_marks))

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n11. Search in List")

cities = ["Delhi", "Mumbai", "Chandigarh", "Shimla"]

search = "Shimla"

if search in cities:
    print(search, "found in list.")
else:
    print(search, "not found.")

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n12. Copying Lists")

list1 = [1, 2, 3, 4]
list2 = list1.copy()

list2.append(5)

print("Original :", list1)
print("Copied   :", list2)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Lists are ordered and mutable.")
print("2. Lists can store different data types.")
print("3. Use append(), insert(), extend() to add items.")
print("4. Use remove(), pop(), del to remove items.")
print("5. sort() arranges elements.")
print("6. reverse() reverses the list.")
print("7. List comprehension creates lists efficiently.")
print("8. Lists are one of Python's most versatile data structures.")

print("\nEnd of Program")