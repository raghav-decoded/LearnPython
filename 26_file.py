'''
    r
        open file for reading : default 
    w
        open file for writing
    x
        creates file if it doesn't exist
    a
        add more content to a file
    t
        text mode: default
    b
        binary mode
    +
        read and write
    
    rt
        read text
    rb
        read binary

    open("filename","mode")
        returns a pointer to the file
        if mode is empty, default r
    read(x)
        read x bytes in the file
        default: read entire file
    readline()
        read a line
    readlines()
        returns a list of all lines

    for line in f:
        print(line, end="")
    close()
'''

f = open("/Users/raghavsingh/Documents/Python_Study/26hello.txt", "r")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()