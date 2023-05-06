'''
OS MODULE

dir(os)
    returns all funcs associated with os mod
getcwd()
    returns cwd
chdir("NEW DIR")
    change cwd 
listdir("PATH")
    returns contents of a dir
makedirs("DIR/SUB-DIR")
    makes dir and a sub dir
mkdir("NAME")
    make a new dir
rename("THIS","THAT")
    renames THIS to THAT
os.environ.get('')
    get environ vars
os.path.join("PATH1","PATH2")
    join paths
os.path.exists("PATH")
    checks if path exists or not
os.path.is___("PATH")
    checks if the path is a  ___ = file/dir...

'''
import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("harry.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("harry.txt", "codewithharry.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/harry.txt"))

# print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))
