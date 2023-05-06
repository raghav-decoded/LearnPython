''' Lambda functions or anonymous functions
    One line functions
    
    list.sort()
'''
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))


a =[[1, 14], [5, 6], [8,23]]
# key is the next index from x
a.sort(key=lambda x:x[1])
print(a)
  
 