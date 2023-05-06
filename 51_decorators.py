'''
Decorators
    A decorator decorates a function

Creating copies of functions
deleting functions
returning functions
passing function as arg
taking a function, modifying it and retuning (decorators)
@decorator_name
    function_name
'''

# Creating copies of functions
def function1():
    print("Subscribe now")
func2 = function1
# deleting functions
del function1
func2()

# returning functions
def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
a = funcret(1)
print(a)

# passing function as arg
def executor(func):
    func("this")
executor(print)

# taking a function, modifying it and returning (decorators)
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

# @dec1 works like *below
@dec1
def who_is_harry():
    print("Harry is a good boy")

# * overwriting the function
#  who_is_harry = dec1(who_is_harry)

who_is_harry()

  
