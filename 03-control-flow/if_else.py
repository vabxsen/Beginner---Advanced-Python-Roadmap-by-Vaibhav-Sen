"""
=========================================================
Topic : If, Else and Conditional Statements in Python
=========================================================

This program demonstrates:
1. Simple if statement
2. if-else statement
3. if-elif-else statement
4. Nested if statements
5. Multiple conditions
6. Logical operators
7. Ternary Operator
8. Pass statement
9. Practical Examples
"""
print("=" * 60)
print("IF, ELSE AND CONDITIONAL STATEMENTS")
print("=" * 60)

# =======================================================
# SIMPLE IF STATEMENT
# =======================================================

age = 20

print("\n1. Simple If Statement")

if age >= 18:
    print("You are eligible to vote.")

# =======================================================
# IF - ELSE STATEMENT
# =======================================================

marks = 35

print("\n2. If-Else Statement")

if marks >= 40:
    print("Result : Pass")
else:
    print("Result : Fail")

# =======================================================
# IF - ELIF - ELSE
# =======================================================

score = 86

print("\n3. If-Elif-Else Statement")

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"

print("Score :", score)
print("Grade :", grade)

# =======================================================
# NESTED IF STATEMENTS
# =======================================================

username = "admin"
password = "python123"

print("\n4. Nested If Statement")

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Unknown User")

# =======================================================
# LOGICAL OPERATORS
# =======================================================

age = 25
citizen = True

print("\n5. Logical Operators")

if age >= 18 and citizen:
    print("Eligible to vote")

if age >= 18 or citizen:
    print("At least one condition is True")

if not citizen:
    print("Not a citizen")
else:
    print("Citizen Verified")

# =======================================================
# MULTIPLE CONDITIONS
# =======================================================

number = 24

print("\n6. Multiple Conditions")

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by both 2 and 3")
else:
    print(number, "is not divisible by both 2 and 3")

# =======================================================
# TERNARY (SHORT-HAND IF)
# =======================================================

salary = 55000

status = "High Salary" if salary >= 50000 else "Normal Salary"

print("\n7. Ternary Operator")
print(status)

# =======================================================
# PASS STATEMENT
# =======================================================

print("\n8. Pass Statement")

value = 5

if value > 0:
    pass        # Placeholder for future code

print("Program continues after pass.")

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

temperature = 32

print("\n9. Weather Example")

if temperature >= 35:
    print("Very Hot")
elif temperature >= 25:
    print("Pleasant Weather")
elif temperature >= 15:
    print("Cool Weather")
else:
    print("Cold Weather")

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

balance = 5000
withdraw = 2500

print("\n10. ATM Example")

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal Successful")
    print("Remaining Balance :", balance)
else:
    print("Insufficient Balance")

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

username = "Cheese"
password = "12345"

print("\n11. Login System")

if username == "Cheese" and password == "12345":
    print("Access Granted")
else:
    print("Access Denied")

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

year = 2024

print("\n12. Leap Year Check")

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. if        -> Executes code when condition is True")
print("2. else      -> Executes when if condition is False")
print("3. elif      -> Checks multiple conditions")
print("4. Nested if -> if inside another if")
print("5. Logical operators -> and, or, not")
print("6. Ternary operator -> One-line conditional statement")
print("7. pass      -> Placeholder statement")

print("\nEnd of Program")