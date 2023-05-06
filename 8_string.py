"""
Strings
    Single Quote String : (‘Single Quote String’)
    Double Quote String : (“Double Quote String”)
    Triple Quote String : (‘’’ Triple Quote String ‘’’)

    len()
        returns the length of the string
    isalnum
        checks if a given string is alphanumeric
    isalpha
        checks if a given string is alphabetic
    
    endswith(str)
        checks if a given string ends with str
    count(str)
        counts the occurence of str
    capitalize()
        capitalizes the first character of the string
    upper()
        converts the string to uppercase
    lower()
        converts the string to lowercase
    find(str)
        finds index of str in the string
    replace(str1, str2)
        replaces a str1 with str2
    
    index
    str1 = "hello"
     0  1  2  3  4 
     h  e  l  l  o
    -5 -4 -3 -2 -1

    length = 5

String slicing
    str1[index] 
        prints the character at the index if index = [0,length]
    str1[0:5]
        prints index 0,1,2,3,4 i.e [0,5)
    str1[1:4]
        prints index 1,2,3,4 i.e [1,4)
    str1[-5:-2]
        prints index -5, -4, -3 i.e [-5,-2)
        = str1[0,3]
    str1[0:]
        prints index 0 to the end of the string
        [X:] R takes the length by default
    str1[:5]
        prints from 0 to 5th index
        [:X] L takes 0 by default

    str1[::2]
        skips every 2nd index
        "hlo"
    str1[::3]
        skips every 3rd index
        "helo"
    str1[:-2:2]
        skips every 2nd index -[5,-2]
        "hl"
    str1[::-1]
        prints every character taken backwards
    str1[::-2]
        prints every second character taken backwards
"""

demo = "Raghav is a good boy" 
print(demo.endswith("boy"))
print(demo.count('oo'))
print(demo.capitalize())
print(demo.upper())
print(demo.lower())
print(demo.find("is"))
print(demo.replace("good","nice"))

str1 = "hello"
'''
     1  2  1  2  1 
     h  e  l  l  o
skip (2-1 = 1) character after reading each character = hlo
'''
print(str1[::2])

'''
     1  2  3  1  2 
     h  e  l  l  o
        x  x     x
skip (3-1 = 2) character after reading each character = hl
'''
print(str1[::3])

'''
     1  2  1  2   
     h  e  l  l  o
    -5 -4 -3 -2 -1
 skip (2-1 = 1) character after reading each character upto -2 index = hl
'''
print(str1[:-2:2])
# if third index is negative,calculation starts from right
print(str1[::-1])
print(str1[::-2])
