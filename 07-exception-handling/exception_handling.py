"""
=========================================================
Topic : Exception Handling in Python
=========================================================

This program demonstrates:
1. try and except
2. Handling Multiple Exceptions
3. else Block
4. finally Block
5. Raising Exceptions
6. Custom Exceptions
7. Nested Exception Handling
8. Practical Examples
"""
print("=" * 60)
print("EXCEPTION HANDLING IN PYTHON")
print("=" * 60)

# =======================================================
# BASIC TRY-EXCEPT
# =======================================================

print("\n1. Basic Try-Except")

try:
    number = 10
    result = number / 0
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# =======================================================
# MULTIPLE EXCEPT BLOCKS
# =======================================================

print("\n2. Multiple Exception Handling")

try:
    number = int("Python")

except ValueError:
    print("ValueError: Invalid integer.")

except TypeError:
    print("TypeError occurred.")

# =======================================================
# HANDLING MULTIPLE EXCEPTIONS TOGETHER
# =======================================================

print("\n3. Multiple Exceptions Together")

try:
    value = int("ABC")
    answer = value / 0

except (ValueError, ZeroDivisionError) as error:
    print("Exception:", error)

# =======================================================
# ELSE BLOCK
# =======================================================

print("\n4. Else Block")

try:
    number = 100
    result = number / 5

except ZeroDivisionError:
    print("Division Error")

else:
    print("Division Successful")
    print("Answer:", result)

# =======================================================
# FINALLY BLOCK
# =======================================================

print("\n5. Finally Block")

try:
    print("Opening Resource...")
    value = 50 / 10

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Closing Resource...")
    print("finally block always executes.")

# =======================================================
# RAISING EXCEPTIONS
# =======================================================

print("\n6. Raising Exception")

age = 15

try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")

except ValueError as error:
    print(error)

# =======================================================
# CUSTOM EXCEPTION
# =======================================================

print("\n7. Custom Exception")

class InvalidSalaryError(Exception):
    """Custom Exception"""
    pass

salary = -5000

try:
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")

except InvalidSalaryError as error:
    print(error)

# =======================================================
# NESTED EXCEPTION HANDLING
# =======================================================

print("\n8. Nested Try-Except")

try:
    number = int("50")

    try:
        result = number / 0

    except ZeroDivisionError:
        print("Inner Exception: Division by zero.")

except ValueError:
    print("Outer Exception: Invalid number.")

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n9. Safe Calculator")

num1 = 20
num2 = 0

try:
    answer = num1 / num2
    print(answer)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n10. Safe List Access")

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index is out of range.")

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n11. Safe Dictionary Access")

student = {
    "name": "Alice",
    "course": "Python"
}

try:
    print(student["age"])

except KeyError:
    print("Key does not exist.")

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n12. File Handling Exception")

try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("sample.txt not found.")

# =======================================================
# PRACTICAL EXAMPLE 5
# =======================================================

print("\n13. Input Validation")

value = "25"

try:
    number = int(value)
    print("Valid Number:", number)

except ValueError:
    print("Invalid Number")

# =======================================================
# PRACTICAL EXAMPLE 6
# =======================================================

print("\n14. General Exception")

try:
    numbers = [1, 2, 3]
    print(numbers[10])

except Exception as error:
    print("An unexpected error occurred.")
    print("Error:", error)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. try       -> Code that may cause an exception.")
print("2. except    -> Handles exceptions.")
print("3. else      -> Executes if no exception occurs.")
print("4. finally   -> Always executes.")
print("5. raise     -> Raises an exception manually.")
print("6. Custom Exceptions improve program readability.")
print("7. Multiple except blocks handle different errors.")
print("8. Exception handling prevents program crashes.")
print("9. Exception as e stores the error message.")
print("10. Good exception handling improves reliability.")

print("\nEnd of Program")