'''Write a Python program to implement concepts of
a) Abstract Methods and Abstract Classes
b) Interfaces

'''
# a) Abstract Methods and Abstract Classes:

'''An abstract class is a class that cannot be instantiated and is used as a blueprint for other
classes. It may contain abstract methods that are declared but not implemented. In Python,
abstract classes and methods are implemented using the abc (Abstract Base Class) module.'''

# Part A: Abstract Class and Abstract Methods

'''
1. Import ABC and abstractmethod from the abc module.
2. Create an abstract class.
3. Define abstract methods inside the abstract class.
4. Create a child class and implement the abstract methods.
'''

from abc import ABC , abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

 
print("Abstract Class and Abstract Method: ")
rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())


# b) Interfaces:

'''Python does not provide interfaces explicitly like Java. However, interfaces can be
implemented using abstract base classes by defining only abstract methods. Any class
that implements an interface must provide implementations for all its methods.'''

# Part B: Interface Implementation

'''
1. Create an interface using an abstract base class.
2. Define only abstract methods.
3. Implement the interface in derived classes.
4. Call methods using object references.
'''


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass    

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


print("Interface Implementation: ")
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()