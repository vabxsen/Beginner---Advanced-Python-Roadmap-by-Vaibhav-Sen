"""
=========================================================
Topic : Polymorphism in Python
=========================================================

This program demonstrates:
1. Method Overriding
2. Duck Typing
3. Operator Overloading
4. Function Polymorphism
5. Polymorphism with Inheritance
6. Built-in Polymorphic Functions
7. Practical Examples
"""

print("=" * 60)
print("POLYMORPHISM IN PYTHON")
print("=" * 60)

# =======================================================
# METHOD OVERRIDING
# =======================================================

class Animal:

    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):

    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):

    def speak(self):
        print("Cat says: Meow!")

print("\n1. Method Overriding")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# =======================================================
# POLYMORPHISM USING A COMMON FUNCTION
# =======================================================

def animal_sound(animal):
    animal.speak()

print("\n2. Runtime Polymorphism")

animal_sound(dog)
animal_sound(cat)

# =======================================================
# DUCK TYPING
# =======================================================

class Duck:

    def walk(self):
        print("Duck is walking.")

class Person:

    def walk(self):
        print("Person is walking.")

def start_walking(obj):
    obj.walk()

print("\n3. Duck Typing")

duck = Duck()
person = Person()

start_walking(duck)
start_walking(person)

# =======================================================
# FUNCTION POLYMORPHISM
# =======================================================

print("\n4. Built-in Polymorphic Functions")

print(len("Python"))
print(len([10, 20, 30, 40]))
print(len((1, 2, 3)))
print(len({"A": 1, "B": 2}))

# =======================================================
# OPERATOR OVERLOADING
# =======================================================

print("\n5. Operator Overloading")

print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])

# =======================================================
# CUSTOM OPERATOR OVERLOADING
# =======================================================

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

print("\n6. Custom Operator Overloading")

v1 = Vector(5, 10)
v2 = Vector(15, 20)

v3 = v1 + v2

print("Vector 1 :", v1)
print("Vector 2 :", v2)
print("Addition :", v3)

# =======================================================
# POLYMORPHISM WITH INHERITANCE
# =======================================================

class Shape:

    def area(self):
        print("Calculating Area")

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle Area =", self.length * self.width)

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area =", 3.14 * self.radius ** 2)

print("\n7. Shape Polymorphism")

shapes = [
    Rectangle(10, 5),
    Circle(7)
]

for shape in shapes:
    shape.area()

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

class Payment:

    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

class Cash(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")

print("\n8. Payment System")

payments = [
    CreditCard(),
    UPI(),
    Cash()
]

for method in payments:
    method.pay(1500)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

class Employee:

    def salary(self):
        pass

class Developer(Employee):

    def salary(self):
        print("Developer Salary : ₹90,000")

class Manager(Employee):

    def salary(self):
        print("Manager Salary : ₹1,20,000")

class Designer(Employee):

    def salary(self):
        print("Designer Salary : ₹70,000")

print("\n9. Employee Salary")

employees = [
    Developer(),
    Manager(),
    Designer()
]

for employee in employees:
    employee.salary()

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Polymorphism means 'Many Forms'.")
print("2. Same method behaves differently for different objects.")
print("3. Method Overriding is Runtime Polymorphism.")
print("4. Duck Typing focuses on behavior, not type.")
print("5. Operators are polymorphic (+ works differently).")
print("6. __add__() overloads the + operator.")
print("7. Built-in functions like len() are polymorphic.")
print("8. Polymorphism increases flexibility.")
print("9. It reduces code duplication.")
print("10. It is one of the four pillars of OOP.")

print("\nEnd of Program")