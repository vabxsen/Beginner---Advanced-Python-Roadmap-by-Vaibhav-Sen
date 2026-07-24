"""
=========================================================
Topic : Pandas in Python
=========================================================

This program demonstrates:
1. Creating Series
2. Creating DataFrames
3. Reading CSV Files
4. Viewing Data
5. Selecting Columns
6. Filtering Data
7. Adding Columns
8. Sorting Data
9. Handling Missing Values
10. Practical Examples

Install Pandas:
pip install pandas
"""

import pandas as pd

print("=" * 60)
print("PANDAS IN PYTHON")
print("=" * 60)

# =======================================================
# SERIES
# =======================================================

print("\n1. Creating Series")

series = pd.Series([10, 20, 30, 40, 50])

print(series)

# =======================================================
# DATAFRAME
# =======================================================

print("\n2. Creating DataFrame")

students = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 21, 22, 23],
    "Course": ["Python", "AI", "DBMS", "ML"],
    "Marks": [90, 85, 95, 88]
}

df = pd.DataFrame(students)

print(df)

# =======================================================
# VIEWING DATA
# =======================================================

print("\n3. Viewing Data")

print("Head:")
print(df.head())

print("\nTail:")
print(df.tail())

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns)

# =======================================================
# DATA INFORMATION
# =======================================================

print("\n4. Data Information")

print(df.info())

print("\nStatistics")
print(df.describe())

# =======================================================
# SELECTING DATA
# =======================================================

print("\n5. Selecting Columns")

print(df["Name"])

print("\nMultiple Columns")

print(df[["Name", "Marks"]])

# =======================================================
# FILTERING
# =======================================================

print("\n6. Filter Students with Marks >= 90")

top_students = df[df["Marks"] >= 90]

print(top_students)

# =======================================================
# ADDING A COLUMN
# =======================================================

print("\n7. Adding Grade Column")

df["Grade"] = ["A", "B", "A+", "A"]

print(df)

# =======================================================
# UPDATING DATA
# =======================================================

print("\n8. Updating Marks")

df.loc[1, "Marks"] = 89

print(df)

# =======================================================
# SORTING
# =======================================================

print("\n9. Sort by Marks")

sorted_df = df.sort_values(by="Marks", ascending=False)

print(sorted_df)

# =======================================================
# HANDLING MISSING VALUES
# =======================================================

print("\n10. Missing Values")

data = {
    "Name": ["John", "Alice", "Bob"],
    "Marks": [90, None, 85]
}

missing_df = pd.DataFrame(data)

print(missing_df)

print("\nFilled Missing Values")

print(missing_df.fillna(0))

# =======================================================
# SAVING TO CSV
# =======================================================

print("\n11. Save DataFrame")

df.to_csv("students.csv", index=False)

print("students.csv saved successfully!")

# =======================================================
# READING CSV
# =======================================================

print("\n12. Read CSV File")

loaded_df = pd.read_csv("students.csv")

print(loaded_df)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n13. Average Marks")

average = df["Marks"].mean()

print("Average Marks:", average)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n14. Highest Scorer")

highest = df[df["Marks"] == df["Marks"].max()]

print(highest)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n15. Student Count")

print("Total Students:", len(df))

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n16. Group by Grade")

grouped = df.groupby("Grade")["Marks"].mean()

print(grouped)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Series is a one-dimensional data structure.")
print("2. DataFrame is a two-dimensional table.")
print("3. read_csv() loads CSV files.")
print("4. to_csv() saves data.")
print("5. head() and tail() preview data.")
print("6. info() shows dataset information.")
print("7. describe() provides statistics.")
print("8. loc[] selects specific rows and columns.")
print("9. groupby() groups similar records.")
print("10. Pandas is the most popular data analysis library.")

print("\nEnd of Program")