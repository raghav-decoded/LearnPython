''' LISTS,TUPLES
    lists = mutable
    tuples = immutable

    empty list
        []   
    integers                                           
        [1, 2, 3]                                
    numbers (integers and floating point)
        [1, 2.5, 3.7, 9]     
    characters
        ['a', 'b', 'c']      
    mixed value types
        ['a', 1, 'b', 3.5, 'zero']  
    strings 
        ['One', 'Two', 'Three']  

Methods
    append(VALUE)
    insert(INDEX,VALUE)
    remove(VALUE)
    pop()
        remove the value at the last index
    reverse()
    sort()
    max()
    min()

Slicing
    seq = list1[start_index:stop_index]

Tuples
    (VALUE,)
        A tuple of one element

Swapping of two numbers 
    a,b = b,a
'''

grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",
           "Lollypop", 56]
# print(grocery[5])
numbers = [2, 7, 9, 11, 3]
# numbers.remove(9)
# numbers.pop()
# numbers.sort()
# numbers = []
# numbers.reverse()
# numbers.append(1)
# numbers.append(72)
# numbers.append(5)
# numbers.insert(2, 67)
# print(numbers)
# 3, 11, 9, 7, 2
# print(numbers)
# numbers[1] = 98
# print(numbers)
# Mutable - can change
# Immutable - cannot change
# tp = (1,)
# print(tp)
a = 1
b = 8
a, b = b,a
# temp = a
# a = b
# b = temp
print(a, b)

