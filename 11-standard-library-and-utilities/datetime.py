"""
=========================================================
Topic : Date and Time in Python
=========================================================

This program demonstrates:
1. Current Date & Time
2. Creating Date Objects
3. Creating Time Objects
4. Creating Datetime Objects
5. Formatting Dates
6. Parsing Strings to Dates
7. Timedelta
8. Date Arithmetic
9. Timestamp
10. Practical Examples
"""

from datetime import datetime, date, time, timedelta

print("=" * 60)
print("DATE AND TIME IN PYTHON")
print("=" * 60)

# =======================================================
# CURRENT DATE AND TIME
# =======================================================

print("\n1. Current Date & Time")

current = datetime.now()

print("Current Date & Time :", current)

# =======================================================
# CURRENT DATE
# =======================================================

print("\n2. Current Date")

today = date.today()

print("Today's Date :", today)
print("Year  :", today.year)
print("Month :", today.month)
print("Day   :", today.day)

# =======================================================
# CURRENT TIME
# =======================================================

print("\n3. Current Time")

current_time = datetime.now().time()

print("Current Time :", current_time)

# =======================================================
# CREATING DATE OBJECTS
# =======================================================

print("\n4. Creating Date Object")

birthday = date(2005, 8, 15)

print("Birthday :", birthday)

# =======================================================
# CREATING TIME OBJECTS
# =======================================================

print("\n5. Creating Time Object")

meeting = time(10, 30, 45)

print("Meeting Time :", meeting)

# =======================================================
# CREATING DATETIME OBJECTS
# =======================================================

print("\n6. Creating Datetime Object")

event = datetime(2026, 12, 25, 18, 30)

print("Event :", event)

# =======================================================
# DATE FORMATTING
# =======================================================

print("\n7. Date Formatting")

print(current.strftime("%d-%m-%Y"))
print(current.strftime("%A"))
print(current.strftime("%B"))
print(current.strftime("%I:%M %p"))
print(current.strftime("%d/%m/%Y %H:%M:%S"))

# =======================================================
# STRING TO DATETIME
# =======================================================

print("\n8. Parsing String")

date_string = "30-06-2026"

parsed = datetime.strptime(date_string, "%d-%m-%Y")

print(parsed)

# =======================================================
# TIMESTAMP
# =======================================================

print("\n9. Timestamp")

timestamp = current.timestamp()

print(timestamp)

# =======================================================
# TIMEDELTA
# =======================================================

print("\n10. Timedelta")

future = current + timedelta(days=10)
past = current - timedelta(days=15)

print("10 Days Later :", future)
print("15 Days Earlier :", past)

# =======================================================
# DIFFERENCE BETWEEN DATES
# =======================================================

print("\n11. Date Difference")

date1 = date(2026, 1, 1)
date2 = date(2026, 12, 31)

difference = date2 - date1

print("Difference :", difference.days, "days")

# =======================================================
# WEEKDAY
# =======================================================

print("\n12. Weekday")

print("Weekday Number :", today.weekday())
print("Weekday Name :", today.strftime("%A"))

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n13. Age Calculator")

birth_date = date(2004, 5, 20)

age = today.year - birth_date.year

print("Birth Date :", birth_date)
print("Approximate Age :", age)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n14. Countdown")

exam = datetime(2026, 12, 31)

remaining = exam - current

print("Days Left :", remaining.days)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n15. Digital Clock Format")

print(current.strftime("%H:%M:%S"))

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n16. Calendar Formats")

formats = [
    "%d-%m-%Y",
    "%m/%d/%Y",
    "%A, %d %B %Y",
    "%I:%M %p",
    "%H:%M:%S"
]

for fmt in formats:
    print(current.strftime(fmt))

# =======================================================
# PRACTICAL EXAMPLE 5
# =======================================================

print("\n17. Add Working Days")

working_day = today + timedelta(days=5)

print("Today :", today)
print("After 5 Days :", working_day)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. datetime.now() -> Current date & time")
print("2. date.today() -> Current date")
print("3. time() -> Create time object")
print("4. datetime() -> Create datetime object")
print("5. strftime() -> Format date & time")
print("6. strptime() -> Parse string into datetime")
print("7. timedelta -> Date arithmetic")
print("8. timestamp() -> Unix timestamp")
print("9. Date subtraction gives timedelta")
print("10. datetime module is widely used in scheduling and logging")

print("\nEnd of Program")