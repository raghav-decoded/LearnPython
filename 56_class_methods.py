'''
decorators

class myClass:
    @classmethod
    def myfunc (cls, arg1, arg2, ...):

classmethod decorator modifies cls, the class it takes as input

'''
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    # This classmethod takes cls ie the class by default
    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

# we need to pass 3 arguments to employee constructor
harry = Employee("Harry", 255, "Instructor")
rohan = Employee("rohan",765,"student")

# using the change_leaves function the value of no_of_leaves changes everywhere
rohan.change_leaves(34)
print(rohan.__dict__)
print(rohan.no_of_leaves)
print(harry.__dict__)
print(harry.no_of_leaves)
print(Employee.__dict__)


