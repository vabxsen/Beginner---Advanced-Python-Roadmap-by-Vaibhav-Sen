"""
=========================================================
Topic : Abstraction in Python
=========================================================

This program demonstrates:
1. What is Abstraction?
2. Abstract Base Classes (ABC)
3. Abstract Methods
4. Implementing Abstract Classes
5. Multiple Abstract Methods
6. Real-World Examples
7. Benefits of Abstraction
"""

from abc import ABC, abstractmethod

print("=" * 60)
print("ABSTRACTION IN PYTHON")
print("=" * 60)

# =======================================================
# ABSTRACT CLASS
# =======================================================

class Animal(ABC):
    """Abstract Base Class"""

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog says: Woof!")

    def move(self):
        print("Dog is Running.")


class Cat(Animal):

    def sound(self):
        print("Cat says: Meow!")

    def move(self):
        print("Cat is Walking.")


print("\n1. Abstract Class Example")

dog = Dog()
cat = Cat()

dog.sound()
dog.move()

cat.sound()
cat.move()

# =======================================================
# ABSTRACT CLASS WITH CONSTRUCTOR
# =======================================================

class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


print("\n2. Abstract Constructor")

rectangle = Rectangle(10, 5, "Blue")

print("Color :", rectangle.color)
print("Area  :", rectangle.area())

# =======================================================
# MULTIPLE ABSTRACT METHODS
# =======================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started.")

    def stop(self):
        print("Car Stopped.")

    def fuel_type(self):
        print("Fuel: Petrol")


print("\n3. Vehicle Example")

car = Car()

car.start()
car.stop()
car.fuel_type()

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


print("\n4. Payment Gateway")

payment1 = CreditCard()
payment2 = UPI()

payment1.pay(1500)
payment2.pay(2500)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass


class Developer(Employee):

    def salary(self):
        print("Developer Salary : ₹90,000")


class Manager(Employee):

    def salary(self):
        print("Manager Salary : ₹1,20,000")


print("\n5. Employee Salary")

developer = Developer()
manager = Manager()

developer.salary()
manager.salary()

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class MySQL(Database):

    def connect(self):
        print("Connected to MySQL Database.")

    def disconnect(self):
        print("Disconnected from MySQL.")


print("\n6. Database Connection")

database = MySQL()

database.connect()
database.disconnect()

# =======================================================
# ABSTRACT CLASS RULE
# =======================================================

print("\n7. Abstract Class Rule")

print("""
The following code will produce an error:

shape = Shape("Red")

Reason:
Abstract classes cannot be instantiated directly.
Only child classes implementing all abstract methods
can create objects.
""")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Abstraction hides implementation details.")
print("2. Abstract classes are created using ABC.")
print("3. @abstractmethod declares abstract methods.")
print("4. Child classes must implement all abstract methods.")
print("5. Abstract classes cannot be instantiated.")
print("6. Abstraction improves maintainability.")
print("7. It promotes code consistency.")
print("8. Used in frameworks, APIs, and large applications.")
print("9. Abstraction is one of the four pillars of OOP.")
print("10. It focuses on 'What to do', not 'How to do it'.")

print("\nEnd of Program")