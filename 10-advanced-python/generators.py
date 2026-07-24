"""
=========================================================
Topic : Generators in Python
=========================================================

This program demonstrates:
1. What are Generators?
2. yield Keyword
3. Generator Functions
4. Generator Expressions
5. next() Function
6. Generator vs List
7. Infinite Generators
8. Practical Examples
"""

print("=" * 60)
print("GENERATORS IN PYTHON")
print("=" * 60)

# =======================================================
# SIMPLE GENERATOR
# =======================================================

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print("\n1. Simple Generator")

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

# =======================================================
# ITERATING OVER A GENERATOR
# =======================================================

print("\n2. Looping Through Generator")

for value in numbers():
    print(value)

# =======================================================
# GENERATOR WITH RANGE
# =======================================================

def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number

print("\n3. Even Number Generator")

for even in even_numbers(20):
    print(even)

# =======================================================
# GENERATOR EXPRESSION
# =======================================================

print("\n4. Generator Expression")

squares = (x ** 2 for x in range(1, 6))

for square in squares:
    print(square)

# =======================================================
# GENERATOR VS LIST
# =======================================================

print("\n5. Generator vs List")

list_data = [x for x in range(5)]
generator_data = (x for x in range(5))

print("List      :", list_data)
print("Generator :", generator_data)

# =======================================================
# FIBONACCI GENERATOR
# =======================================================

def fibonacci(limit):
    first = 0
    second = 1

    for _ in range(limit):
        yield first
        first, second = second, first + second

print("\n6. Fibonacci Generator")

for number in fibonacci(10):
    print(number)

# =======================================================
# COUNTDOWN GENERATOR
# =======================================================

def countdown(start):

    while start > 0:
        yield start
        start -= 1

print("\n7. Countdown")

for value in countdown(5):
    print(value)

# =======================================================
# INFINITE GENERATOR
# =======================================================

def infinite_numbers():

    number = 1

    while True:
        yield number
        number += 1

print("\n8. Infinite Generator")

generator = infinite_numbers()

for i in range(10):
    print(next(generator))

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

def cube_generator(limit):

    for number in range(1, limit + 1):
        yield number ** 3

print("\n9. Cube Generator")

for cube in cube_generator(5):
    print(cube)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

def names():

    student_names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma"
    ]

    for student in student_names:
        yield student

print("\n10. Student Generator")

for student in names():
    print(student)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

def vowels(text):

    vowels = "AEIOUaeiou"

    for character in text:
        if character in vowels:
            yield character

print("\n11. Vowel Generator")

for vowel in vowels("Python Programming"):
    print(vowel)

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

def powers_of_two(limit):

    value = 1

    while value <= limit:
        yield value
        value *= 2

print("\n12. Powers of Two")

for power in powers_of_two(64):
    print(power)

# =======================================================
# PRACTICAL EXAMPLE 5
# =======================================================

def countdown_timer(seconds):

    while seconds >= 0:
        yield seconds
        seconds -= 1

print("\n13. Countdown Timer")

for second in countdown_timer(5):
    print(second)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Generators produce values one at a time.")
print("2. yield pauses the function and saves its state.")
print("3. next() gets the next generated value.")
print("4. Generator expressions use ().")
print("5. Generators are memory efficient.")
print("6. They are ideal for large datasets.")
print("7. Infinite generators produce endless values.")
print("8. Generators are faster than lists for sequential processing.")
print("9. Generator functions automatically return iterators.")
print("10. Widely used in data processing and file handling.")

print("\nEnd of Program")