'''
Abstract Method 

An abstract method forces its child to include that method

Abstract methods are defined in the abstract class.
An abstract class can have both abstract methods as well as concrete methods.
The abstract class works as a template for other classes. 
Using the abstract class, we can define a structure without properly implementing every method. 
It is not possible to create objects of an abstract class because Abstract class cannot be instantiated.
An error will occur if the abstract method has not been implemented in the derived class.
'''
 
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

# Metaclass ABC
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle" 
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

