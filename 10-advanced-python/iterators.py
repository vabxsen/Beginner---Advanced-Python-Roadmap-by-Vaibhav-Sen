"""
=========================================================
Topic : Iterators in Python
=========================================================

This program demonstrates:
1. What are Iterators?
2. iter() Function
3. next() Function
4. Iterating Manually
5. Iterator with Loops
6. Custom Iterator
7. StopIteration Exception
8. Infinite Iterator
9. Practical Examples
"""

print("=" * 60)
print("ITERATORS IN PYTHON")
print("=" * 60)

# =======================================================
# ITERABLE VS ITERATOR
# =======================================================

print("\n1. Iterable vs Iterator")

numbers = [10, 20, 30, 40, 50]

print("Iterable:", numbers)

iterator = iter(numbers)

print("Iterator Created:", iterator)

# =======================================================
# USING next()
# =======================================================

print("\n2. next() Function")

print(next(iterator))
print(next(iterator))
print(next(iterator))

# =======================================================
# LOOPING THROUGH ITERATOR
# =======================================================

print("\n3. Iterating Using Loop")

fruits = ["Apple", "Banana", "Mango"]

fruit_iterator = iter(fruits)

for fruit in fruit_iterator:
    print(fruit)

# =======================================================
# STOP ITERATION
# =======================================================

print("\n4. StopIteration Exception")

colors = ["Red", "Green"]

color_iterator = iter(colors)

try:
    while True:
        print(next(color_iterator))
except StopIteration:
    print("Iterator Finished!")

# =======================================================
# CUSTOM ITERATOR
# =======================================================

class CountNumbers:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration

print("\n5. Custom Iterator")

counter = CountNumbers(5)

for number in counter:
    print(number)

# =======================================================
# ITERATOR WITH STRINGS
# =======================================================

print("\n6. String Iterator")

language = "Python"

string_iterator = iter(language)

for character in string_iterator:
    print(character)

# =======================================================
# ITERATOR WITH TUPLES
# =======================================================

print("\n7. Tuple Iterator")

subjects = ("Python", "DBMS", "AI", "CN")

subject_iterator = iter(subjects)

for subject in subject_iterator:
    print(subject)

# =======================================================
# INFINITE ITERATOR
# =======================================================

class InfiniteNumbers:

    def __init__(self):
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.number
        self.number += 1
        return value

print("\n8. Infinite Iterator")

infinite = InfiniteNumbers()

for i in range(5):
    print(next(infinite))

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

class EvenNumbers:

    def __init__(self, limit):
        self.number = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.number <= self.limit:
            even = self.number
            self.number += 2
            return even

        raise StopIteration

print("\n9. Even Number Iterator")

for even in EvenNumbers(20):
    print(even)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n10. Manual Iteration")

data = [100, 200, 300]

iterator = iter(data)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

students = ["Alice", "Bob", "Charlie"]

print("\n11. Student Iterator")

student_iterator = iter(students)

try:
    while True:
        print(next(student_iterator))
except StopIteration:
    print("No More Students!")

# =======================================================
# BUILT-IN ITERABLE OBJECTS
# =======================================================

print("\n12. Built-in Iterables")

objects = [
    [1, 2, 3],
    (10, 20),
    "Python",
    {"A", "B"},
    {"Name": "Alice"}
]

for obj in objects:
    print(type(obj).__name__, "is iterable.")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Iterable -> Object that can be iterated.")
print("2. Iterator -> Object that returns one value at a time.")
print("3. iter() creates an iterator.")
print("4. next() retrieves the next value.")
print("5. StopIteration ends iteration.")
print("6. Custom iterators implement __iter__() and __next__().")
print("7. Iterators save memory by producing values on demand.")
print("8. Lists, tuples, strings, sets, and dictionaries are iterable.")
print("9. Infinite iterators should be used carefully.")
print("10. Iterators are widely used in Python libraries.")

print("\nEnd of Program")