"""
=========================================================
Topic : CSV Files in Python
=========================================================

This program demonstrates:
1. Writing to CSV Files
2. Reading CSV Files
3. CSV Reader
4. CSV Writer
5. DictReader
6. DictWriter
7. Appending Data
8. Exception Handling
9. Practical Examples

Module Used:
csv
"""

import csv

print("=" * 60)
print("CSV FILE HANDLING IN PYTHON")
print("=" * 60)

# =======================================================
# WRITING TO CSV
# =======================================================

print("\n1. Writing CSV File")

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Course", "Marks"])

    writer.writerow([101, "Alice", "Python", 91])
    writer.writerow([102, "Bob", "AI", 88])
    writer.writerow([103, "Charlie", "DBMS", 95])

print("students.csv created successfully!")

# =======================================================
# READING CSV
# =======================================================

print("\n2. Reading CSV File")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# =======================================================
# DICTREADER
# =======================================================

print("\n3. DictReader Example")

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"], "-", row["Marks"])

# =======================================================
# APPENDING DATA
# =======================================================

print("\n4. Appending Data")

with open("students.csv", "a", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([104, "David", "Machine Learning", 93])

print("New Student Added!")

# =======================================================
# DICTWRITER
# =======================================================

print("\n5. DictWriter Example")

employees = [
    {"ID": 1, "Name": "John", "Department": "HR"},
    {"ID": 2, "Name": "Emma", "Department": "IT"},
    {"ID": 3, "Name": "James", "Department": "Finance"}
]

with open("employees.csv", "w", newline="") as file:

    fields = ["ID", "Name", "Department"]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()

    writer.writerows(employees)

print("employees.csv created!")

# =======================================================
# READING EMPLOYEE CSV
# =======================================================

print("\n6. Employee Records")

with open("employees.csv", "r") as file:

    reader = csv.DictReader(file)

    for employee in reader:
        print(employee)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n7. Student Report")

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for student in reader:

        print(
            student["Name"],
            "scored",
            student["Marks"],
            "marks."
        )

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n8. Average Marks")

marks = []

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for student in reader:
        marks.append(int(student["Marks"]))

average = sum(marks) / len(marks)

print("Average Marks:", round(average, 2))

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n9. Highest Scorer")

highest = 0
topper = ""

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for student in reader:

        if int(student["Marks"]) > highest:

            highest = int(student["Marks"])
            topper = student["Name"]

print("Topper:", topper)
print("Marks :", highest)

# =======================================================
# EXCEPTION HANDLING
# =======================================================

print("\n10. Exception Handling")

try:

    with open("unknown.csv", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("CSV File Not Found!")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. csv.writer() writes CSV files.")
print("2. csv.reader() reads CSV files.")
print("3. DictWriter writes dictionaries.")
print("4. DictReader reads dictionaries.")
print("5. writerow() writes one row.")
print("6. writerows() writes multiple rows.")
print("7. writeheader() writes column headers.")
print("8. CSV stores tabular data.")
print("9. newline='' prevents blank lines.")
print("10. CSV is widely used for data exchange.")

print("\nEnd of Program")