"""
=========================================================
Topic : Argparse in Python
=========================================================

This program demonstrates:
1. Creating ArgumentParser
2. Positional Arguments
3. Optional Arguments
4. Default Values
5. Required Arguments
6. Choices
7. Boolean Flags
8. Multiple Arguments
9. Help Messages
10. Practical Examples

Run Examples:
python argparse_demo.py Alice
python argparse_demo.py Alice --age 21
python argparse_demo.py Alice --age 21 --course Python
python argparse_demo.py Alice --verbose
"""

import argparse

print("=" * 60)
print("ARGPARSE IN PYTHON")
print("=" * 60)

# =======================================================
# CREATE PARSER
# =======================================================

parser = argparse.ArgumentParser(
    description="Python Argparse Tutorial"
)

# =======================================================
# POSITIONAL ARGUMENT
# =======================================================

parser.add_argument(
    "name",
    help="Enter your name"
)

# =======================================================
# OPTIONAL ARGUMENTS
# =======================================================

parser.add_argument(
    "--age",
    type=int,
    default=18,
    help="Enter your age"
)

parser.add_argument(
    "--course",
    default="Python",
    help="Course Name"
)

# =======================================================
# BOOLEAN FLAG
# =======================================================

parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable Verbose Mode"
)

# =======================================================
# CHOICES
# =======================================================

parser.add_argument(
    "--grade",
    choices=["A", "B", "C", "D"],
    default="A",
    help="Student Grade"
)

# =======================================================
# MULTIPLE VALUES
# =======================================================

parser.add_argument(
    "--marks",
    nargs="+",
    type=int,
    help="Enter Student Marks"
)

# =======================================================
# PARSE ARGUMENTS
# =======================================================

args = parser.parse_args()

# =======================================================
# DISPLAY VALUES
# =======================================================

print("\nStudent Information")
print("-" * 30)

print("Name   :", args.name)
print("Age    :", args.age)
print("Course :", args.course)
print("Grade  :", args.grade)

if args.verbose:
    print("Verbose Mode : ON")

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

if args.marks:

    total = sum(args.marks)

    average = total / len(args.marks)

    print("\nMarks :", args.marks)
    print("Total :", total)
    print("Average :", round(average, 2))

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

if args.age >= 18:
    print("Status : Adult")
else:
    print("Status : Minor")

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

if args.grade == "A":
    print("Performance : Excellent")

elif args.grade == "B":
    print("Performance : Good")

elif args.grade == "C":
    print("Performance : Average")

else:
    print("Performance : Needs Improvement")

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\nWelcome,", args.name)

print(f"You are enrolled in {args.course}.")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. ArgumentParser() creates a parser.")
print("2. add_argument() adds command-line arguments.")
print("3. Positional arguments are mandatory.")
print("4. Optional arguments start with '--'.")
print("5. default sets default values.")
print("6. choices restrict allowed values.")
print("7. action='store_true' creates boolean flags.")
print("8. nargs allows multiple values.")
print("9. parse_args() reads user input.")
print("10. Argparse is widely used for CLI applications.")

print("\nEnd of Program")