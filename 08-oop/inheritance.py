"""
=========================================================
Topic : Inheritance in Python
=========================================================

This program demonstrates:
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. super() Function
6. Method Overriding
7. isinstance() and issubclass()
8. Practical Examples
"""
print("=" * 60)
print("INHERITANCE IN PYTHON")
print("=" * 60)

# =======================================================
# SINGLE INHERITANCE
# =======================================================

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):

    def bark(self):
        print(f"{self.name} is barking.")

print("\n1. Single Inheritance")

dog = Dog("Tommy")
dog.eat()
dog.bark()

# =======================================================
# MULTILEVEL INHERITANCE
# =======================================================

class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def drive(self):
        print("Car is Driving")

class SportsCar(Car):

    def turbo(self):
        print("Turbo Mode Activated!")

print("\n2. Multilevel Inheritance")

ferrari = SportsCar()
ferrari.start()
ferrari.drive()
ferrari.turbo()

# =======================================================
# MULTIPLE INHERITANCE
# =======================================================

class Camera:

    def take_photo(self):
        print("Photo Captured")

class Phone:

    def call(self):
        print("Calling...")

class SmartPhone(Camera, Phone):

    def internet(self):
        print("Browsing Internet")

print("\n3. Multiple Inheritance")

device = SmartPhone()

device.take_photo()
device.call()
device.internet()

# =======================================================
# HIERARCHICAL INHERITANCE
# =======================================================

class Employee:

    def work(self):
        print("Employee is Working")

class Developer(Employee):

    def code(self):
        print("Writing Python Code")

class Designer(Employee):

    def design(self):
        print("Designing UI")

print("\n4. Hierarchical Inheritance")

developer = Developer()
designer = Designer()

developer.work()
developer.code()

designer.work()
designer.design()

# =======================================================
# SUPER() FUNCTION
# =======================================================

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Course : {self.course}")

print("\n5. super() Function")

student = Student("Alice", "Computer Science")
student.display()

# =======================================================
# METHOD OVERRIDING
# =======================================================

class Bird:

    def sound(self):
        print("Bird makes a sound.")

class Sparrow(Bird):

    def sound(self):
        print("Sparrow Chirps.")

print("\n6. Method Overriding")

bird = Sparrow()
bird.sound()

# =======================================================
# isinstance() AND issubclass()
# =======================================================

print("\n7. Built-in Functions")

print(isinstance(student, Student))
print(isinstance(student, Person))
print(issubclass(Student, Person))
print(issubclass(Dog, Animal))

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):

    def add_interest(self):
        self.balance += self.balance * 0.05
        print("Interest Added")

print("\n8. Savings Account")

account = SavingsAccount("John", 10000)

account.show_balance()
account.add_interest()
account.show_balance()

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

class Shape:

    def area(self):
        print("Calculating Area")

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area =", self.length * self.width)

print("\n9. Shape Example")

rectangle = Rectangle(12, 5)
rectangle.area()

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Inheritance allows one class to inherit another.")
print("2. Parent Class is also called Base/Super Class.")
print("3. Child Class is also called Derived/Sub Class.")
print("4. super() calls the parent class constructor/method.")
print("5. Method Overriding changes inherited behavior.")
print("6. Single Inheritance -> One Parent, One Child.")
print("7. Multilevel -> Grandparent -> Parent -> Child.")
print("8. Multiple -> Multiple Parent Classes.")
print("9. Hierarchical -> One Parent, Multiple Children.")
print("10. Inheritance promotes code reuse.")

print("\nEnd of Program")