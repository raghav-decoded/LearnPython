'''
raise
if test_condition:
raise EXCEPTION_CLASS_NAME

try and except block are for handling exceptions, 
the raise keyword, on the contrary, is to raise an exception.

ZeroDivisionError()
     Raised when the second argument of a division is zero.
ValueError()
    Raised when a function receives an argument with the right type but an inappropriate value.
EOFError (End Of File Error): 
    Raised when the input() function hits an end-of-file condition without reading any data.
ImportError: 
    Raised when the import statement has trouble trying to load a module.
NameError: 
    Raised when a local or global name is not found.
KeyError: 
    Raised when a mapping key is not found in the set of existing keys.
'''
# a = input("What is your name")
# b = input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")
# 1000 lines taking 1 hour

# Task - Write about 2 built in exception

c = input("Enter your name")
try:
    print(a)

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")

