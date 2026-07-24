"""
=========================================================
Topic : Encapsulation in Python
=========================================================

This program demonstrates:
1. What is Encapsulation?
2. Public Members
3. Protected Members
4. Private Members
5. Getter Methods
6. Setter Methods
7. Property Decorator (@property)
8. Name Mangling
9. Practical Examples
"""

print("=" * 60)
print("ENCAPSULATION IN PYTHON")
print("=" * 60)

# =======================================================
# PUBLIC MEMBERS
# =======================================================

class Student:

    def __init__(self, name, age):
        self.name = name      # Public
        self.age = age

print("\n1. Public Members")

student = Student("Alice", 20)

print(student.name)
print(student.age)

# =======================================================
# PROTECTED MEMBERS
# =======================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary     # Protected

print("\n2. Protected Members")

employee = Employee("John", 50000)

print(employee.name)
print(employee._salary)

# =======================================================
# PRIVATE MEMBERS
# =======================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

print("\n3. Private Members")

account = BankAccount("Alice", 25000)

print(account.owner)

# This will produce an error
# print(account.__balance)

account.show_balance()

# =======================================================
# GETTER & SETTER METHODS
# =======================================================

class Person:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age")

print("\n4. Getter & Setter")

person = Person(21)

print("Current Age:", person.get_age())

person.set_age(25)

print("Updated Age:", person.get_age())

# =======================================================
# PROPERTY DECORATOR
# =======================================================

class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):

        if value > 0:
            self.__price = value
        else:
            print("Invalid Price")

print("\n5. Property Decorator")

laptop = Product(65000)

print("Price:", laptop.price)

laptop.price = 70000

print("Updated Price:", laptop.price)

# =======================================================
# NAME MANGLING
# =======================================================

print("\n6. Name Mangling")

print(account._BankAccount__balance)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

class ATM:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)

print("\n7. ATM Example")

atm = ATM(10000)

atm.deposit(2500)
atm.withdraw(3000)
atm.show_balance()

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

class MobilePhone:

    def __init__(self):
        self.__battery = 100

    def use_phone(self):
        self.__battery -= 20

    def charge(self):
        self.__battery = 100

    def battery_status(self):
        print("Battery:", self.__battery, "%")

print("\n8. Mobile Phone")

phone = MobilePhone()

phone.use_phone()
phone.use_phone()
phone.battery_status()

phone.charge()
phone.battery_status()

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

class Exam:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100")

    def get_marks(self):
        return self.__marks

print("\n9. Student Marks")

exam = Exam()

exam.set_marks(92)

print("Marks:", exam.get_marks())

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Encapsulation protects object data.")
print("2. Public members are accessible everywhere.")
print("3. Protected members use a single underscore (_).")
print("4. Private members use double underscores (__).")
print("5. Getter methods retrieve private data.")
print("6. Setter methods validate and modify data.")
print("7. @property provides controlled access.")
print("8. Name mangling prevents accidental access.")
print("9. Encapsulation improves security.")
print("10. It is one of the four pillars of OOP.")

print("\nEnd of Program")