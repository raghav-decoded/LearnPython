'''
    break
        move to the end of the loop
    continue
        move to the end of the loop
'''

while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue
