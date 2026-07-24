"""
=========================================================
Topic : Recursion in Python
=========================================================

This program demonstrates:
1. What is Recursion?
2. Base Case
3. Recursive Case
4. Factorial
5. Fibonacci Series
6. Sum of Natural Numbers
7. Power Calculation
8. String Reversal
9. Binary Search
10. Practical Examples
"""

print("=" * 60)
print("RECURSION IN PYTHON")
print("=" * 60)

# =======================================================
# BASIC RECURSION
# =======================================================

print("\n1. Basic Recursion")

def countdown(number):
    if number == 0:              # Base Case
        print("Done!")
        return

    print(number)
    countdown(number - 1)        # Recursive Call

countdown(5)

# =======================================================
# FACTORIAL
# =======================================================

print("\n2. Factorial")

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

print("5! =", factorial(5))
print("7! =", factorial(7))

# =======================================================
# FIBONACCI SERIES
# =======================================================

print("\n3. Fibonacci Series")

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(10):
    print(fibonacci(i), end=" ")

print()

# =======================================================
# SUM OF NATURAL NUMBERS
# =======================================================

print("\n4. Sum of Natural Numbers")

def natural_sum(number):

    if number == 1:
        return 1

    return number + natural_sum(number - 1)

print("Sum =", natural_sum(10))

# =======================================================
# POWER OF A NUMBER
# =======================================================

print("\n5. Power Calculation")

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print("2^5 =", power(2, 5))
print("3^4 =", power(3, 4))

# =======================================================
# STRING REVERSAL
# =======================================================

print("\n6. Reverse String")

def reverse(text):

    if len(text) == 0:
        return ""

    return reverse(text[1:]) + text[0]

word = "Python"

print("Original :", word)
print("Reversed :", reverse(word))

# =======================================================
# PALINDROME CHECK
# =======================================================

print("\n7. Palindrome Check")

def palindrome(text):

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])

print("madam :", palindrome("madam"))
print("python:", palindrome("python"))

# =======================================================
# BINARY SEARCH
# =======================================================

print("\n8. Recursive Binary Search")

numbers = [10, 20, 30, 40, 50, 60, 70]

def binary_search(array, left, right, target):

    if left > right:
        return -1

    middle = (left + right) // 2

    if array[middle] == target:
        return middle

    if target < array[middle]:
        return binary_search(array, left, middle - 1, target)

    return binary_search(array, middle + 1, right, target)

index = binary_search(numbers, 0, len(numbers)-1, 50)

print("50 Found at Index:", index)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n9. Count Digits")

def count_digits(number):

    if number < 10:
        return 1

    return 1 + count_digits(number // 10)

print("Digits in 987654 =", count_digits(987654))

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n10. Find Maximum")

def maximum(values):

    if len(values) == 1:
        return values[0]

    largest = maximum(values[1:])

    if values[0] > largest:
        return values[0]

    return largest

numbers = [45, 82, 99, 12, 77]

print("Largest Number:", maximum(numbers))

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n11. Print Numbers")

def print_numbers(start, end):

    if start > end:
        return

    print(start)

    print_numbers(start + 1, end)

print_numbers(1, 5)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Recursion is when a function calls itself.")
print("2. Every recursive function needs a base case.")
print("3. The recursive case solves smaller sub-problems.")
print("4. Missing a base case causes RecursionError.")
print("5. Recursion is useful for trees and graphs.")
print("6. Factorial and Fibonacci are classic examples.")
print("7. Binary Search is efficiently implemented recursively.")
print("8. Recursive solutions are often elegant.")
print("9. Excessive recursion can increase memory usage.")
print("10. Python has a recursion depth limit.")

print("\nEnd of Program")