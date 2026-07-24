"""
=========================================================
Topic : Operators in Python
=========================================================

This program demonstrates:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
8. Operator Precedence
"""
# =======================================================
# ARITHMETIC OPERATORS
# =======================================================

a = 15
b = 4

print("===== Arithmetic Operators =====")
print("a =", a, "b =", b)
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponentiation :", a ** b)

print()

# =======================================================
# ASSIGNMENT OPERATORS
# =======================================================

x = 10

print("===== Assignment Operators =====")
print("Initial Value :", x)

x += 5
print("After += 5 :", x)

x -= 3
print("After -= 3 :", x)

x *= 2
print("After *= 2 :", x)

x /= 4
print("After /= 4 :", x)

print()

# =======================================================
# COMPARISON OPERATORS
# =======================================================

num1 = 20
num2 = 15

print("===== Comparison Operators =====")
print("num1 == num2 :", num1 == num2)
print("num1 != num2 :", num1 != num2)
print("num1 > num2  :", num1 > num2)
print("num1 < num2  :", num1 < num2)
print("num1 >= num2 :", num1 >= num2)
print("num1 <= num2 :", num1 <= num2)

print()

# =======================================================
# LOGICAL OPERATORS
# =======================================================

age = 22
has_id = True

print("===== Logical Operators =====")
print("Eligible (AND):", age >= 18 and has_id)
print("Child OR Senior:", age < 18 or age > 60)
print("NOT has_id:", not has_id)

print()

# =======================================================
# IDENTITY OPERATORS
# =======================================================

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("===== Identity Operators =====")
print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 == list3     :", list1 == list3)
print("list1 is not list3 :", list1 is not list3)

print()

# =======================================================
# MEMBERSHIP OPERATORS
# =======================================================

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("===== Membership Operators =====")
print("'Apple' in fruits      :", "Apple" in fruits)
print("'Grapes' in fruits     :", "Grapes" in fruits)
print("'Banana' not in fruits :", "Banana" not in fruits)

print()

# =======================================================
# BITWISE OPERATORS
# =======================================================

m = 5      # Binary: 0101
n = 3      # Binary: 0011

print("===== Bitwise Operators =====")
print("m & n :", m & n)
print("m | n :", m | n)
print("m ^ n :", m ^ n)
print("~m    :", ~m)
print("m << 1:", m << 1)
print("m >> 1:", m >> 1)

print()

# =======================================================
# OPERATOR PRECEDENCE
# =======================================================

result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print("===== Operator Precedence =====")
print("10 + 5 * 2     =", result1)
print("(10 + 5) * 2   =", result2)

print()

# =======================================================
# PRACTICAL EXAMPLE
# =======================================================

marks = 85

passed = marks >= 40
distinction = marks >= 75

print("===== Student Result =====")
print("Marks:", marks)
print("Passed:", passed)
print("Distinction:", distinction)

print()

# =======================================================
# SUMMARY
# =======================================================

print("Arithmetic Operators : Perform mathematical calculations")
print("Assignment Operators : Assign or update values")
print("Comparison Operators : Compare two values")
print("Logical Operators    : Combine multiple conditions")
print("Identity Operators   : Compare object identity")
print("Membership Operators : Check presence in a sequence")
print("Bitwise Operators    : Operate on binary values")
print("Operator Precedence  : Determines evaluation order")