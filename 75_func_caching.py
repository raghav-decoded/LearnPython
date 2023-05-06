'''
function caching
Some function calls are repeated
caching helps storing that call and prevent extra calculations
'''
import time
from functools import lru_cache

#decorator lru_cache(maxsize = value), stores last value calls
@lru_cache(maxsize=2)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    # some_work(6)
    # some_work(2)
    print("Done... Calling again")
    # input()
    some_work(4)
    print("Called again")

