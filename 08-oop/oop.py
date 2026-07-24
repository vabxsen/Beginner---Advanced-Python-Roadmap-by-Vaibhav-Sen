"""
=========================================================
Topic : Object-Oriented Programming (OOP) in Python
=========================================================

This program demonstrates:
1. Classes and Objects
2. Constructors (__init__)
3. Instance Variables
4. Class Variables
5. Instance Methods
6. Class Methods
7. Static Methods
8. Object Deletion
9. Built-in Class Functions
10. Practical Examples
"""
print("=" * 60)
print("OBJECT ORIENTED PROGRAMMING (OOP)")
print("=" * 60)

# =======================================================
# DEFINING A CLASS
# =======================================================

class Student:
    """A simple Student class."""

    # Class Variable
    school = "ABC Engineering College"

    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Instance Method
    def display(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print(f"School : {Student.school}")

# =======================================================
# CREATING OBJECTS
# =======================================================

print("\n1. Creating Objects")

student1 = Student("Alice", 21, "Computer Science")
student2 = Student("Bob", 22, "Information Technology")

student1.display()
print()

student2.display()

# =======================================================
# ACCESSING OBJECT ATTRIBUTES
# =======================================================

print("\n2. Accessing Attributes")

print(student1.name)
print(student1.age)
print(student1.course)

# =======================================================
# MODIFYING OBJECT ATTRIBUTES
# =======================================================

print("\n3. Modifying Attributes")

student1.age = 23

print("Updated Age:", student1.age)

# =======================================================
# CLASS VARIABLES
# =======================================================

print("\n4. Class Variable")

print(Student.school)

Student.school = "National University"

print(student1.school)
print(student2.school)

# =======================================================
# CLASS METHOD
# =======================================================

class Employee:

    company = "OpenAI"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, company_name):
        cls.company = company_name

employee1 = Employee("John")

print("\n5. Class Method")

print(Employee.company)

Employee.change_company("Google")

print(Employee.company)

# =======================================================
# STATIC METHOD
# =======================================================

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print("\n6. Static Method")

print("Addition:", Calculator.add(10, 20))

# =======================================================
# BUILT-IN CLASS FUNCTIONS
# =======================================================

print("\n7. Built-in Functions")

print(isinstance(student1, Student))
print(type(student1))
print(hasattr(student1, "name"))
print(getattr(student1, "course"))
setattr(student1, "age", 24)
print(student1.age)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def details(self):
        print(f"{self.brand} {self.model} ({self.year})")

print("\n8. Car Class")

car = Car("Toyota", "Fortuner", 2024)

car.details()

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.balance)

print("\n9. Bank Account")

account = BankAccount("Alice", 10000)

account.deposit(2500)
account.withdraw(3000)
account.show_balance()

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

print("\n10. Rectangle")

rectangle = Rectangle(10, 5)

print("Area:", rectangle.area())

# =======================================================
# OBJECT DELETION
# =======================================================

print("\n11. Object Deletion")

temporary = Student("Temp", 20, "Python")

print("Object Created")

del temporary

print("Object Deleted")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Class is a blueprint for creating objects.")
print("2. Object is an instance of a class.")
print("3. __init__() is the constructor.")
print("4. self refers to the current object.")
print("5. Instance variables belong to individual objects.")
print("6. Class variables are shared among all objects.")
print("7. Instance methods work with object data.")
print("8. @classmethod works with class data.")
print("9. @staticmethod doesn't access class/object data.")
print("10. OOP improves code organization and reusability.")

print("\nEnd of Program")