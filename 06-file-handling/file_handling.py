"""
=========================================================
Topic : File Handling in Python
=========================================================

This program demonstrates:
1. Opening Files
2. Reading Files
3. Writing Files
4. Appending Data
5. File Modes
6. with Statement
7. File Methods
8. Checking File Information
9. Exception Handling
10. Practical Examples
"""
import os

print("=" * 60)
print("FILE HANDLING IN PYTHON")
print("=" * 60)

# =======================================================
# WRITING TO A FILE
# =======================================================

print("\n1. Writing to a File")

with open("student.txt", "w") as file:
    file.write("Name : Alice\n")
    file.write("Age : 21\n")
    file.write("Course : Computer Science\n")

print("Data written successfully!")

# =======================================================
# READING A FILE
# =======================================================

print("\n2. Reading a File")

with open("student.txt", "r") as file:
    content = file.read()

print(content)

# =======================================================
# READING LINE BY LINE
# =======================================================

print("\n3. Reading Line by Line")

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())

# =======================================================
# APPENDING DATA
# =======================================================

print("\n4. Appending Data")

with open("student.txt", "a") as file:
    file.write("CGPA : 9.2\n")

print("New data appended.")

# =======================================================
# READLINES()
# =======================================================

print("\n5. readlines()")

with open("student.txt", "r") as file:
    lines = file.readlines()

print(lines)

# =======================================================
# FILE MODES
# =======================================================

print("\n6. File Modes")

print("r  -> Read")
print("w  -> Write (Overwrite)")
print("a  -> Append")
print("x  -> Create New File")
print("rb -> Read Binary")
print("wb -> Write Binary")

# =======================================================
# FILE INFORMATION
# =======================================================

print("\n7. File Information")

if os.path.exists("student.txt"):
    print("File Exists")
    print("File Size:", os.path.getsize("student.txt"), "bytes")
else:
    print("File does not exist.")

# =======================================================
# EXCEPTION HANDLING
# =======================================================

print("\n8. Exception Handling")

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: data.txt does not exist.")

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n9. Store Student Marks")

marks = [85, 90, 78, 92, 88]

with open("marks.txt", "w") as file:
    for mark in marks:
        file.write(str(mark) + "\n")

print("Marks saved successfully.")

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n10. Calculate Average Marks")

total = 0
count = 0

with open("marks.txt", "r") as file:
    for line in file:
        total += int(line)
        count += 1

average = total / count

print("Average Marks:", average)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n11. Count Lines in a File")

with open("student.txt", "r") as file:
    total_lines = len(file.readlines())

print("Total Lines:", total_lines)

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n12. Copy File")

with open("student.txt", "r") as source:
    data = source.read()

with open("student_copy.txt", "w") as destination:
    destination.write(data)

print("File copied successfully.")

# =======================================================
# PRACTICAL EXAMPLE 5
# =======================================================

print("\n13. Create Multiple Records")

students = [
    "John,90",
    "Alice,95",
    "Bob,88",
    "Charlie,91"
]

with open("records.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("Records Created.")

# =======================================================
# PRACTICAL EXAMPLE 6
# =======================================================

print("\n14. Read Student Records")

with open("records.txt", "r") as file:
    for record in file:
        name, marks = record.strip().split(",")
        print(f"Name: {name:<10} Marks: {marks}")

# =======================================================
# DELETE FILE (OPTIONAL)
# =======================================================

print("\n15. Delete a File")

filename = "temporary.txt"

with open(filename, "w") as file:
    file.write("Temporary File")

if os.path.exists(filename):
    os.remove(filename)
    print(filename, "deleted successfully.")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. open() opens a file.")
print("2. with automatically closes files.")
print("3. read() reads the whole file.")
print("4. readline() reads one line.")
print("5. readlines() returns a list of lines.")
print("6. write() writes data.")
print("7. append() adds new data.")
print("8. Exception handling prevents crashes.")
print("9. os.path.exists() checks file existence.")
print("10. os.remove() deletes files.")

print("\nEnd of Program")