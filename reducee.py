#from functools import reduce     import functools--->functools.reduce(func_ name,iterate)
from functools import reduce
def my_max(x,y):
    if x>=y:
        return x
    else:
        return y
l1=eval(input("enter any"))
p=reduce(my_max,l1)
print(p)