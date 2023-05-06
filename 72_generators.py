"""
Generators

return = returns a value and stops
print = prints a value to the output window
yield = yields a value in an active process

iterable objects
    str list tuple

__iter__()
    returns an iterable object

Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - process

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = (546546,8788)
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
