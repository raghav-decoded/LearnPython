'''
if we use functions in a program in another program
all actions will be performed automatically 

making a main function avoids such problems
only the called functions are used 

if __name__ == '__main__':
    body

__name__ is main for the base/parent program
__name__ is the base/parent program if the file gets imported
'''
def printhar(string):
    return f"Ye string harry ko de de thakur {string}"

def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__)

if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)
  
