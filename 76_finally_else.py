'''
finally
    runs no matter try/except get executed or not
    used for "cleaning up"

else
    runs if except doesn't run
'''
f1 = open("harry.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
