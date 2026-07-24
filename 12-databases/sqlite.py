"""
=========================================================
Topic : SQLite Database in Python
=========================================================

This program demonstrates:
1. Connecting to SQLite Database
2. Creating a Table
3. Inserting Records
4. Reading Records
5. Updating Records
6. Deleting Records
7. Using WHERE Clause
8. Parameterized Queries
9. Exception Handling
10. Closing the Connection
"""

import sqlite3

print("=" * 60)
print("SQLITE DATABASE IN PYTHON")
print("=" * 60)

# =======================================================
# CONNECT TO DATABASE
# =======================================================

print("\n1. Connecting to Database")

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

print("Database Connected Successfully!")

# =======================================================
# CREATE TABLE
# =======================================================

print("\n2. Creating Table")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    cgpa REAL
)
""")

connection.commit()

print("Table Created Successfully!")

# =======================================================
# INSERT RECORDS
# =======================================================

print("\n3. Inserting Records")

students = [
    ("Alice", 21, "Python", 8.9),
    ("Bob", 22, "AI", 9.2),
    ("Charlie", 20, "DBMS", 8.5)
]

cursor.executemany("""
INSERT INTO students(name, age, course, cgpa)
VALUES (?, ?, ?, ?)
""", students)

connection.commit()

print("Records Inserted Successfully!")

# =======================================================
# READ RECORDS
# =======================================================

print("\n4. Displaying Records")

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for row in records:
    print(row)

# =======================================================
# UPDATE RECORD
# =======================================================

print("\n5. Updating Record")

cursor.execute("""
UPDATE students
SET cgpa = ?
WHERE name = ?
""", (9.5, "Alice"))

connection.commit()

print("Record Updated!")

# =======================================================
# SEARCH USING WHERE
# =======================================================

print("\n6. Search Record")

cursor.execute("""
SELECT * FROM students
WHERE course = ?
""", ("AI",))

results = cursor.fetchall()

for student in results:
    print(student)

# =======================================================
# DELETE RECORD
# =======================================================

print("\n7. Delete Record")

cursor.execute("""
DELETE FROM students
WHERE name = ?
""", ("Charlie",))

connection.commit()

print("Record Deleted!")

# =======================================================
# COUNT RECORDS
# =======================================================

print("\n8. Count Records")

cursor.execute("SELECT COUNT(*) FROM students")

count = cursor.fetchone()[0]

print("Total Students:", count)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n9. Students with CGPA >= 9")

cursor.execute("""
SELECT name, cgpa
FROM students
WHERE cgpa >= 9
""")

for student in cursor.fetchall():
    print(student)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n10. Sorting Records")

cursor.execute("""
SELECT *
FROM students
ORDER BY cgpa DESC
""")

for student in cursor.fetchall():
    print(student)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n11. Display Student Names")

cursor.execute("""
SELECT name
FROM students
""")

for student in cursor.fetchall():
    print(student[0])

# =======================================================
# EXCEPTION HANDLING
# =======================================================

print("\n12. Exception Handling")

try:

    cursor.execute("""
    INSERT INTO students(name, age, course, cgpa)
    VALUES (?, ?, ?, ?)
    """, ("David", 23, "Machine Learning", 8.8))

    connection.commit()

    print("Record Added Successfully!")

except sqlite3.Error as error:

    print("Database Error:", error)

# =======================================================
# FINAL RECORDS
# =======================================================

print("\n13. Final Database Contents")

cursor.execute("SELECT * FROM students")

for student in cursor.fetchall():
    print(student)

# =======================================================
# CLOSE CONNECTION
# =======================================================

print("\n14. Closing Connection")

cursor.close()
connection.close()

print("Database Connection Closed!")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. sqlite3.connect() -> Connect to database")
print("2. cursor() -> Execute SQL statements")
print("3. CREATE TABLE -> Create a new table")
print("4. INSERT -> Add records")
print("5. SELECT -> Retrieve records")
print("6. UPDATE -> Modify existing records")
print("7. DELETE -> Remove records")
print("8. WHERE -> Filter records")
print("9. commit() -> Save changes")
print("10. close() -> Close the database connection")

print("\nEnd of Program")