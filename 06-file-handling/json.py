"""
=========================================================
Topic : JSON in Python
=========================================================

This program demonstrates:
1. Python Dictionary to JSON
2. JSON to Python Dictionary
3. Writing JSON to a File
4. Reading JSON from a File
5. Pretty Printing JSON
6. Nested JSON
7. Accessing JSON Data
8. Modifying JSON
9. Exception Handling
10. Practical Examples

Module Used:
json
"""

import json

print("=" * 60)
print("JSON IN PYTHON")
print("=" * 60)

# =======================================================
# PYTHON DICTIONARY TO JSON
# =======================================================

print("\n1. Dictionary to JSON")

student = {
    "id": 101,
    "name": "Alice",
    "age": 21,
    "course": "Python",
    "marks": 92
}

json_data = json.dumps(student)

print(json_data)

# =======================================================
# PRETTY PRINT JSON
# =======================================================

print("\n2. Pretty JSON")

pretty_json = json.dumps(student, indent=4)

print(pretty_json)

# =======================================================
# JSON TO PYTHON DICTIONARY
# =======================================================

print("\n3. JSON to Dictionary")

json_string = '''
{
    "name":"Bob",
    "age":22,
    "city":"Delhi"
}
'''

python_dict = json.loads(json_string)

print(python_dict)
print("Name:", python_dict["name"])

# =======================================================
# WRITING JSON TO FILE
# =======================================================

print("\n4. Writing JSON File")

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("student.json created successfully.")

# =======================================================
# READING JSON FILE
# =======================================================

print("\n5. Reading JSON File")

with open("student.json", "r") as file:
    data = json.load(file)

print(data)

# =======================================================
# ACCESSING JSON DATA
# =======================================================

print("\n6. Accessing Values")

print("Student Name :", data["name"])
print("Course       :", data["course"])

# =======================================================
# MODIFYING JSON DATA
# =======================================================

print("\n7. Modifying JSON")

data["marks"] = 98
data["city"] = "Mumbai"

print(json.dumps(data, indent=4))

# =======================================================
# NESTED JSON
# =======================================================

print("\n8. Nested JSON")

employee = {
    "id": 201,
    "name": "John",
    "department": {
        "name": "IT",
        "floor": 5
    },
    "skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ]
}

print(json.dumps(employee, indent=4))

print("Department:", employee["department"]["name"])
print("Skill:", employee["skills"][0])

# =======================================================
# EXCEPTION HANDLING
# =======================================================

print("\n9. Exception Handling")

invalid_json = '{"name":"Alice","age":20'

try:
    json.loads(invalid_json)

except json.JSONDecodeError as error:
    print("JSON Error:", error)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n10. Student Database")

students = [
    {"name": "Alice", "marks": 90},
    {"name": "Bob", "marks": 84},
    {"name": "Charlie", "marks": 95}
]

print(json.dumps(students, indent=4))

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n11. Search Student")

for student in students:

    if student["name"] == "Charlie":
        print(student)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n12. Average Marks")

total = sum(student["marks"] for student in students)

average = total / len(students)

print("Average:", average)

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n13. Add New Student")

students.append({
    "name": "David",
    "marks": 91
})

print(json.dumps(students, indent=4))

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. dumps() converts Python object to JSON string.")
print("2. loads() converts JSON string to Python object.")
print("3. dump() writes JSON to a file.")
print("4. load() reads JSON from a file.")
print("5. indent formats JSON output.")
print("6. JSON stores structured data.")
print("7. JSON is widely used in APIs.")
print("8. Dictionaries become JSON objects.")
print("9. Lists become JSON arrays.")
print("10. JSON is language-independent.")

print("\nEnd of Program")