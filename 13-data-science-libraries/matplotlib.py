"""
=========================================================
Topic : Matplotlib in Python
=========================================================

This program demonstrates:
1. Line Chart
2. Bar Chart
3. Horizontal Bar Chart
4. Pie Chart
5. Scatter Plot
6. Histogram
7. Titles and Labels
8. Grid
9. Legend
10. Practical Examples

Install Matplotlib:
pip install matplotlib
"""

import matplotlib.pyplot as plt

print("=" * 60)
print("MATPLOTLIB IN PYTHON")
print("=" * 60)

# =======================================================
# LINE CHART
# =======================================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 140, 120, 170, 200]

plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker="o", linewidth=2)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# =======================================================
# BAR CHART
# =======================================================

subjects = ["Python", "DBMS", "AI", "CN"]
marks = [90, 85, 95, 88]

plt.figure(figsize=(6, 4))
plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# =======================================================
# HORIZONTAL BAR CHART
# =======================================================

languages = ["Python", "Java", "C++", "JavaScript"]
students = [60, 40, 30, 50]

plt.figure(figsize=(6, 4))
plt.barh(languages, students)
plt.title("Programming Language Popularity")
plt.show()

# =======================================================
# PIE CHART
# =======================================================

sizes = [45, 25, 20, 10]
labels = ["Python", "Java", "C++", "Others"]

plt.figure(figsize=(6, 6))
plt.pie(sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Programming Language Usage")
plt.show()

# =======================================================
# SCATTER PLOT
# =======================================================

height = [150, 155, 160, 165, 170, 175]
weight = [45, 50, 55, 60, 68, 72]

plt.figure(figsize=(6, 4))
plt.scatter(height, weight)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()

# =======================================================
# HISTOGRAM
# =======================================================

marks = [65, 72, 80, 81, 90, 92, 75, 84, 88, 95]

plt.figure(figsize=(6, 4))
plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# =======================================================
# MULTIPLE LINES
# =======================================================

months = ["Jan", "Feb", "Mar", "Apr"]

product_a = [20, 25, 28, 30]
product_b = [18, 22, 27, 35]

plt.figure(figsize=(6, 4))

plt.plot(months, product_a,
         marker="o",
         label="Product A")

plt.plot(months, product_b,
         marker="s",
         label="Product B")

plt.title("Product Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True)
plt.show()

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

students = ["Alice", "Bob", "Charlie", "David"]
marks = [90, 82, 96, 88]

plt.figure(figsize=(6, 4))
plt.bar(students, marks)
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

temperature = [28, 30, 32, 35, 33, 31, 29]

days = ["Mon", "Tue", "Wed",
        "Thu", "Fri", "Sat", "Sun"]

plt.figure(figsize=(6, 4))
plt.plot(days, temperature, marker="o")
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

expenses = [3500, 1500, 2500, 1000]

categories = ["Food",
              "Transport",
              "Shopping",
              "Other"]

plt.figure(figsize=(6, 6))
plt.pie(expenses,
        labels=categories,
        autopct="%1.1f%%")

plt.title("Monthly Expenses")
plt.show()

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. plot() -> Line Graph")
print("2. bar() -> Vertical Bar Chart")
print("3. barh() -> Horizontal Bar Chart")
print("4. scatter() -> Scatter Plot")
print("5. hist() -> Histogram")
print("6. pie() -> Pie Chart")
print("7. title() -> Chart Title")
print("8. xlabel() / ylabel() -> Axis Labels")
print("9. legend() -> Show Legend")
print("10. show() -> Display Graph")

print("\nEnd of Program")