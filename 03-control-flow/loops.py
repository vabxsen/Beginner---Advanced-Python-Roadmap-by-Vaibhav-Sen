"""
=========================================================
Topic : Loops in Python
=========================================================

This program demonstrates:
1. for loop
2. while loop
3. range() function
4. Nested loops
5. break statement
6. continue statement
7. pass statement
8. Loop else
9. Pattern Printing
10. Practical Examples
"""
print("=" * 60)
print("LOOPS IN PYTHON")
print("=" * 60)

# =======================================================
# FOR LOOP
# =======================================================

print("\n1. Simple For Loop")

for i in range(1, 6):
    print("Iteration:", i)

# =======================================================
# RANGE FUNCTION
# =======================================================

print("\n2. Range Function")

print("range(5):")
for i in range(5):
    print(i, end=" ")

print("\n\nrange(2, 8):")
for i in range(2, 8):
    print(i, end=" ")

print("\n\nrange(0, 11, 2):")
for i in range(0, 11, 2):
    print(i, end=" ")

print()

# =======================================================
# LOOPING THROUGH A STRING
# =======================================================

print("\n3. Loop Through String")

language = "Python"

for letter in language:
    print(letter)

# =======================================================
# WHILE LOOP
# =======================================================

print("\n4. While Loop")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1

# =======================================================
# BREAK STATEMENT
# =======================================================

print("\n5. Break Statement")

for number in range(1, 11):
    if number == 6:
        print("Loop stopped at", number)
        break
    print(number)

# =======================================================
# CONTINUE STATEMENT
# =======================================================

print("\n6. Continue Statement")

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print("Odd Number:", number)

# =======================================================
# PASS STATEMENT
# =======================================================

print("\n7. Pass Statement")

for i in range(3):
    if i == 1:
        pass
    print(i)

# =======================================================
# LOOP ELSE
# =======================================================

print("\n8. Loop Else")

for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully!")

# =======================================================
# NESTED LOOPS
# =======================================================

print("\n9. Nested Loops")

for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row},{column})", end=" ")
    print()

# =======================================================
# PATTERN PRINTING
# =======================================================

print("\n10. Star Pattern")

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# =======================================================
# MULTIPLICATION TABLE
# =======================================================

print("\n11. Multiplication Table of 7")

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# =======================================================
# SUM OF NUMBERS
# =======================================================

print("\n12. Sum of First 10 Numbers")

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)

# =======================================================
# FACTORIAL
# =======================================================

print("\n13. Factorial")

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} =", factorial)

# =======================================================
# PRACTICAL EXAMPLE
# =======================================================

print("\n14. Find Even Numbers")

numbers = [12, 7, 9, 18, 24, 31, 42]

for num in numbers:
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

# =======================================================
# INFINITE LOOP (COMMENTED)
# =======================================================

"""
while True:
    print("This loop runs forever!")
"""

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. for loop        -> Iterate over sequences")
print("2. while loop      -> Execute until condition becomes False")
print("3. range()         -> Generate number sequences")
print("4. break           -> Exit loop immediately")
print("5. continue        -> Skip current iteration")
print("6. pass            -> Placeholder statement")
print("7. else with loop  -> Runs after loop finishes normally")
print("8. Nested loops    -> Loop inside another loop")
print("9. Patterns        -> Common use of nested loops")
print("10. Practical uses -> Tables, factorials, sums, searching")

print("\nEnd of Program")