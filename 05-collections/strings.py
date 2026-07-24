"""
=========================================================
Topic : Strings in Python
=========================================================

This program demonstrates:
1. Creating Strings
2. String Indexing
3. String Slicing
4. String Methods
5. String Formatting
6. Escape Characters
7. Membership Operators
8. String Iteration
9. String Concatenation
10. Practical Examples
"""
print("=" * 60)
print("STRINGS IN PYTHON")
print("=" * 60)

# =======================================================
# CREATING STRINGS
# =======================================================

name = "Alice"
language = 'Python'
message = """Python is
an easy and
powerful language."""

print("\n1. Creating Strings")
print(name)
print(language)
print(message)

# =======================================================
# STRING INDEXING
# =======================================================

print("\n2. String Indexing")

text = "Programming"

print("First Character :", text[0])
print("Last Character  :", text[-1])
print("Fourth Character:", text[3])

# =======================================================
# STRING SLICING
# =======================================================

print("\n3. String Slicing")

print("First 5 Characters :", text[:5])
print("Last 4 Characters  :", text[-4:])
print("Middle Characters  :", text[3:8])
print("Every 2nd Character:", text[::2])

# =======================================================
# STRING METHODS
# =======================================================

print("\n4. Common String Methods")

sentence = "python programming"

print("Original :", sentence)
print("Upper    :", sentence.upper())
print("Lower    :", sentence.lower())
print("Title    :", sentence.title())
print("Capitalize:", sentence.capitalize())
print("Replace  :", sentence.replace("python", "Java"))
print("Count 'm':", sentence.count("m"))
print("Find 'pro':", sentence.find("pro"))
print("Startswith:", sentence.startswith("python"))
print("Endswith :", sentence.endswith("ing"))

# =======================================================
# REMOVING WHITESPACES
# =======================================================

print("\n5. Strip Methods")

data = "   Hello Python   "

print("Before :", repr(data))
print("After  :", repr(data.strip()))

# =======================================================
# STRING CONCATENATION
# =======================================================

print("\n6. Concatenation")

first = "Hello"
second = "World"

result = first + " " + second

print(result)

# =======================================================
# STRING FORMATTING
# =======================================================

print("\n7. String Formatting")

name = "Vaibhav"
age = 21
cgpa = 8.75

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My CGPA is {cgpa:.2f}")

# =======================================================
# ESCAPE CHARACTERS
# =======================================================

print("\n8. Escape Characters")

print("Hello\nWorld")
print("Python\tProgramming")
print("He said, \"Python is awesome!\"")

# =======================================================
# MEMBERSHIP OPERATORS
# =======================================================

print("\n9. Membership Operators")

language = "Python Programming"

print("Python" in language)
print("Java" in language)

# =======================================================
# ITERATING THROUGH A STRING
# =======================================================

print("\n10. Loop Through String")

for character in "Python":
    print(character)

# =======================================================
# SPLIT AND JOIN
# =======================================================

print("\n11. Split and Join")

sentence = "Apple,Banana,Mango"

fruits = sentence.split(",")

print(fruits)

joined = " | ".join(fruits)

print(joined)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n12. Palindrome Checker")

word = "madam"

if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n13. Reverse String")

text = "Python"

print("Original :", text)
print("Reversed :", text[::-1])

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n14. Count Vowels")

text = "Python Programming"

vowels = "aeiouAEIOU"

count = 0

for char in text:
    if char in vowels:
        count += 1

print("Text :", text)
print("Total Vowels :", count)

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n15. Character Frequency")

word = "programming"

frequency = {}

for char in word:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Strings are immutable.")
print("2. Strings support indexing and slicing.")
print("3. Common methods: upper(), lower(), title(), replace().")
print("4. strip() removes extra spaces.")
print("5. split() converts a string into a list.")
print("6. join() combines list elements into a string.")
print("7. f-strings provide readable string formatting.")
print("8. Strings can be iterated using loops.")
print("9. Strings are widely used for text processing.")
print("10. Strings are one of Python's most important data types.")

print("\nEnd of Program")