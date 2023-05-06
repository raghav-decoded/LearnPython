'''
self
    self is used to refer to an object
    it automatically takes the object and performs operations

constructors
    __init__(self,a1,a2,a3...):
        body
a constructor is used to initialize an object
__init__ is not called explicitly, it is automatically called when we pass arguments to the class
'''

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(harry.salary)

