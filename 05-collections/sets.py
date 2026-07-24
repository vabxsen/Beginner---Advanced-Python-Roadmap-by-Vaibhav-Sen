"""
=========================================================
Topic : Sets in Python
=========================================================

This program demonstrates:
1. Creating Sets
2. Adding Elements
3. Removing Elements
4. Set Operations
5. Membership Operators
6. Looping Through Sets
7. Set Methods
8. Frozen Sets
9. Practical Examples
"""
print("=" * 60)
print("SETS IN PYTHON")
print("=" * 60)

# =======================================================
# CREATING SETS
# =======================================================

numbers = {10, 20, 30, 40, 50}
fruits = {"Apple", "Banana", "Mango", "Orange"}

print("\n1. Creating Sets")
print(numbers)
print(fruits)

# Duplicate values are removed automatically
duplicate_numbers = {1, 2, 3, 3, 4, 4, 5}

print("\nDuplicate values are removed automatically:")
print(duplicate_numbers)

# Empty Set
empty_set = set()

print("\nEmpty Set:")
print(empty_set)

# =======================================================
# ADDING ELEMENTS
# =======================================================

print("\n2. Adding Elements")

fruits.add("Pineapple")
print("After add():", fruits)

fruits.update(["Kiwi", "Papaya", "Cherry"])
print("After update():", fruits)

# =======================================================
# REMOVING ELEMENTS
# =======================================================

print("\n3. Removing Elements")

fruits.remove("Kiwi")
print("After remove():", fruits)

fruits.discard("Dragon Fruit")   # No error if not found

removed = fruits.pop()           # Removes random element

print("Random Removed:", removed)
print("Current Set:", fruits)

# =======================================================
# SET OPERATIONS
# =======================================================

print("\n4. Set Operations")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# =======================================================
# MEMBERSHIP OPERATORS
# =======================================================

print("\n5. Membership Operators")

print("3 in set1 :", 3 in set1)
print("10 in set1:", 10 in set1)

# =======================================================
# LOOPING THROUGH SETS
# =======================================================

print("\n6. Iterating Through Sets")

for item in set1:
    print(item)

# =======================================================
# SET METHODS
# =======================================================

print("\n7. Useful Set Methods")

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print("Subset:", A.issubset(B))
print("Superset:", B.issuperset(A))
print("Disjoint:", A.isdisjoint({8, 9}))

# =======================================================
# COPYING & CLEARING
# =======================================================

print("\n8. Copying Sets")

copy_set = set1.copy()

print("Copied Set:", copy_set)

copy_set.clear()

print("After clear():", copy_set)

# =======================================================
# FROZEN SET
# =======================================================

print("\n9. Frozen Set")

immutable_set = frozenset([10, 20, 30])

print(immutable_set)

# immutable_set.add(40)  # Error

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n10. Remove Duplicate Values")

marks = [80, 75, 80, 90, 75, 95, 100]

unique_marks = set(marks)

print("Original List :", marks)
print("Unique Marks  :", unique_marks)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n11. Common Subjects")

student1 = {"Math", "Physics", "Python", "DBMS"}
student2 = {"Python", "Math", "AI", "Java"}

common = student1.intersection(student2)

print("Student 1:", student1)
print("Student 2:", student2)
print("Common Subjects:", common)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n12. Unique Characters")

text = "programming"

letters = set(text)

print("Word:", text)
print("Unique Letters:", letters)
print("Total Unique Letters:", len(letters))

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Sets are unordered collections.")
print("2. Sets do not allow duplicate values.")
print("3. Sets are mutable.")
print("4. add() adds a single element.")
print("5. update() adds multiple elements.")
print("6. remove() removes an element.")
print("7. discard() removes safely without errors.")
print("8. Union combines two sets.")
print("9. Intersection returns common elements.")
print("10. Difference returns unique elements.")
print("11. Symmetric Difference returns non-common elements.")
print("12. Frozen Sets are immutable.")

print("\nEnd of Program")