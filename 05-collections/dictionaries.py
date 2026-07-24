"""
=========================================================
Topic : Dictionaries in Python
=========================================================

This program demonstrates:
1. Creating Dictionaries
2. Accessing Values
3. Adding & Updating Items
4. Removing Items
5. Dictionary Methods
6. Looping Through Dictionaries
7. Nested Dictionaries
8. Dictionary Comprehension
9. Copying Dictionaries
10. Practical Examples
"""
print("=" * 60)
print("DICTIONARIES IN PYTHON")
print("=" * 60)

# =======================================================
# CREATING DICTIONARIES
# =======================================================

student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science",
    "cgpa": 8.9
}

print("\n1. Creating Dictionary")
print(student)

# =======================================================
# ACCESSING VALUES
# =======================================================

print("\n2. Accessing Values")

print("Name :", student["name"])
print("Age  :", student.get("age"))
print("Course :", student.get("course"))

# =======================================================
# ADDING & UPDATING ITEMS
# =======================================================

print("\n3. Adding & Updating Items")

student["city"] = "Delhi"
student["cgpa"] = 9.2

print(student)

# =======================================================
# REMOVING ITEMS
# =======================================================

print("\n4. Removing Items")

student.pop("city")
print("After pop():", student)

student["phone"] = "9876543210"

removed_item = student.popitem()
print("popitem() removed:", removed_item)

del student["age"]

print("After del:", student)

# =======================================================
# DICTIONARY METHODS
# =======================================================

print("\n5. Dictionary Methods")

print("Keys   :", student.keys())
print("Values :", student.values())
print("Items  :", student.items())

# =======================================================
# LOOPING THROUGH DICTIONARIES
# =======================================================

print("\n6. Looping Through Dictionary")

for key, value in student.items():
    print(f"{key} : {value}")

# =======================================================
# NESTED DICTIONARIES
# =======================================================

print("\n7. Nested Dictionary")

students = {
    "Student1": {
        "name": "Alice",
        "marks": 91
    },
    "Student2": {
        "name": "Bob",
        "marks": 85
    }
}

print(students)

print("\nStudent Records:")

for key, value in students.items():
    print(key, "->", value)

# =======================================================
# DICTIONARY COMPREHENSION
# =======================================================

print("\n8. Dictionary Comprehension")

squares = {x: x * x for x in range(1, 6)}

print(squares)

# =======================================================
# COPYING DICTIONARIES
# =======================================================

print("\n9. Copy Dictionary")

copy_student = student.copy()

print("Original:", student)
print("Copied  :", copy_student)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n10. Student Report Card")

report = {
    "Name": "Vaibhav",
    "Python": 95,
    "DBMS": 90,
    "CN": 88,
    "AI": 92
}

total = report["Python"] + report["DBMS"] + report["CN"] + report["AI"]

average = total / 4

print("Student:", report["Name"])
print("Total Marks:", total)
print("Average:", average)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n11. Inventory System")

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

inventory["Monitor"] = 8
inventory["Mouse"] += 5

for item, quantity in inventory.items():
    print(f"{item} -> {quantity}")

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n12. Word Frequency Counter")

sentence = "python is easy and python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n13. Employee Database")

employee = {
    "ID": 101,
    "Name": "John",
    "Department": "IT",
    "Salary": 65000
}

for key, value in employee.items():
    print(f"{key:<12}: {value}")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Dictionaries store data as key-value pairs.")
print("2. Keys must be unique and immutable.")
print("3. Values can be of any data type.")
print("4. get() safely retrieves values.")
print("5. update() modifies existing data.")
print("6. pop() removes a specific key.")
print("7. popitem() removes the last inserted item.")
print("8. keys(), values(), items() are useful methods.")
print("9. Dictionary comprehension creates dictionaries efficiently.")
print("10. Dictionaries are widely used in APIs, JSON, databases, and applications.")

print("\nEnd of Program")