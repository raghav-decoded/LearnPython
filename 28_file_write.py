'''
    w
        write to a file
        creates file if it doesn't exist
        returns characters printed
    a
        append in a file
        creates file if it doesn't exist
    r+
        read/write in existing file

'''
# f = open("/Users/raghavsingh/Documents/Python_Study/raghav.txt", "w")
# a = f.write("rago bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("/Users/raghavsingh/Documents/Python_Study/raghav.txt", "a")
# a = f.write("Rago bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("/Users/raghavsingh/Documents/Python_Study/26hello.txt", "r+")
print(f.read())
f.write("thank you") 
f.close()

