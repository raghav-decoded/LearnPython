# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object


# Task:
a =[6, 4 , "34"]
b = [6, 4 , "34"]
print(b is a) #False

c = [1, 2, 3]
d = [1, 2, 3]
print(c == d) #True
print(c is d) #False

f = c 
print(c == f) #True
print(c is f) #True