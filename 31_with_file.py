'''
    with open("filename") as f:
        body
    
    with closes file automatically

    f = open("filename")
    f.close()
'''

with open("/Users/raghavsingh/Documents/Python_Study/26hello.txt") as f:
    a = f.readlines()
    print(a)

# f = open("/Users/raghavsingh/Documents/Python_Study/26hello.txt", "rt")
#Question of the day - Yes or No and why?
# f.close()
  
