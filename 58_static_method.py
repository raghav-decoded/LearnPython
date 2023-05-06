'''
static method
    works like class functions
    we do not need the self or cls to be passed as the first argument in a static method.

Differences between Class Method and Static Method:

    Taking a class or, in short, form cls as an argument is a must for a class method.
    With the help of class methods, we can change and alter the variables of the class.
    Class methods are restricted to OOPs, so we can only use them if a class exists.
    We generally use class methods to create factory methods. 
        Factory methods return a class object which is similar to a constructor for different use cases.
    
    There is no such restriction of any specific parameter related to class in the Static method.
    With a static method, we can not change or alter the class state.
    The static method is not restricted to a class.
    Static methods are used to create utility functions.
'''
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

Employee.printgood("Rohan")


