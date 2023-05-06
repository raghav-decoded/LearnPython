'''
class variables are variables which are the same for every object
instance variables are declared for a specific object

__dict__
    prints all variables associated with a class
'''
# no_of_leaves is a class variable
class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
# The value of no_of_leaves class variable is now 9
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)

# the no_of_leaves for object rohan is 7
rohan.no_of_leaves = 7
print(rohan.__dict__)
