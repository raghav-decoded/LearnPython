'''
    time module

    time()
        returns the time as a floating point number expressed in seconds since the epoch, in UTC.
    sleep(SECONDS)
        delays by SECONDS
    time.localtime( time.time() )
        returns a tuple of the local time
    time.asctime( time.localtime(time.time() ))
        returns the local time in format 
'''
import time
initial = time.time()

k = 0
while(k<45):
    print("This is harry bhai")
    time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 =time.time()
for i in range(45):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "Seconds")


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
  
