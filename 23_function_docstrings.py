'''
    Functions 
        Built-in
        User defined

    def function_name(arg1,arg2,arg3...):
        """docstring"""
        body
        return value
    
    A function can have 0 args and no return statement

    docstring
        A docstring is the first comment in the function
        It gives a documentary of the function when called
        print(function_name.__doc__)
'''
# a = 9
# b = 8
# c = sum((a, b)) # built in function

def function1(a, b):
    print("Hello you are in function 1", a+b)

def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

# v = function2(5, 7)
# print(v)
print(function2.__doc__)
