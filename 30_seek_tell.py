'''
    tell()
        tells the position of the file handle
    seek(value)
        resets the position to value
'''
f = open("/Users/raghavsingh/Documents/Python_Study/26hello.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
  
