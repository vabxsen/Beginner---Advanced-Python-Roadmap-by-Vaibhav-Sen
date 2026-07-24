"""
=========================================================
Topic : Regular Expressions (Regex) in Python
=========================================================

This program demonstrates:
1. Importing re Module
2. re.search()
3. re.match()
4. re.findall()
5. re.finditer()
6. re.sub()
7. re.split()
8. Character Classes
9. Quantifiers
10. Practical Examples
"""

import re

print("=" * 60)
print("REGULAR EXPRESSIONS (REGEX)")
print("=" * 60)

# =======================================================
# SEARCH
# =======================================================

print("\n1. re.search()")

text = "Python is a powerful programming language."

result = re.search("powerful", text)

if result:
    print("Word Found:", result.group())
    print("Starts At :", result.start())
    print("Ends At   :", result.end())

# =======================================================
# MATCH
# =======================================================

print("\n2. re.match()")

text = "Python Programming"

result = re.match("Python", text)

if result:
    print("Matched:", result.group())

# =======================================================
# FINDALL
# =======================================================

print("\n3. re.findall()")

sentence = "Apple Mango Apple Banana Apple"

words = re.findall("Apple", sentence)

print(words)
print("Total Matches:", len(words))

# =======================================================
# FINDITER
# =======================================================

print("\n4. re.finditer()")

for match in re.finditer("Python", "Python Java Python C++ Python"):
    print("Found at index:", match.start())

# =======================================================
# SUBSTITUTE
# =======================================================

print("\n5. re.sub()")

text = "I love Java."

updated = re.sub("Java", "Python", text)

print(updated)

# =======================================================
# SPLIT
# =======================================================

print("\n6. re.split()")

data = "Apple,Banana;Mango Orange"

result = re.split("[,; ]", data)

print(result)

# =======================================================
# CHARACTER CLASSES
# =======================================================

print("\n7. Character Classes")

text = "Python123 Java456 C789"

print("Digits:", re.findall(r"\d+", text))
print("Words :", re.findall(r"[A-Za-z]+", text))
print("Numbers & Words:", re.findall(r"\w+", text))

# =======================================================
# QUANTIFIERS
# =======================================================

print("\n8. Quantifiers")

sentence = "Hellooo Hiiii Heyyy"

print(re.findall(r"He\w+", sentence))
print(re.findall(r"Hi+", sentence))

# =======================================================
# EMAIL VALIDATION
# =======================================================

print("\n9. Email Validation")

email = "student@gmail.com"

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

# =======================================================
# PHONE NUMBER VALIDATION
# =======================================================

print("\n10. Phone Number Validation")

phone = "9876543210"

if re.fullmatch(r"\d{10}", phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

# =======================================================
# PASSWORD VALIDATION
# =======================================================

print("\n11. Password Validation")

password = "Python@123"

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

# =======================================================
# EXTRACT NUMBERS
# =======================================================

print("\n12. Extract Numbers")

text = "Laptop ₹80000, Mouse ₹1500, Keyboard ₹3500"

numbers = re.findall(r"\d+", text)

print(numbers)

# =======================================================
# REMOVE EXTRA SPACES
# =======================================================

print("\n13. Remove Extra Spaces")

text = "Python      is     awesome"

clean = re.sub(r"\s+", " ", text)

print(clean)

# =======================================================
# PRACTICAL EXAMPLE
# =======================================================

print("\n14. Extract URLs")

paragraph = """
Visit https://python.org
Visit https://openai.com
Visit https://github.com
"""

urls = re.findall(r"https?://\S+", paragraph)

for url in urls:
    print(url)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. re.search()     -> Searches entire string.")
print("2. re.match()      -> Matches from beginning.")
print("3. re.findall()    -> Returns all matches.")
print("4. re.finditer()   -> Returns iterator of matches.")
print("5. re.sub()        -> Replaces matching text.")
print("6. re.split()      -> Splits string using regex.")
print("7. Character Classes -> \\d, \\w, \\s etc.")
print("8. Quantifiers -> *, +, ?, {m,n}")
print("9. Regex is useful for validation and searching.")
print("10. Widely used in data cleaning and web scraping.")

print("\nEnd of Program")