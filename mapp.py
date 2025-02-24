# def sqr(n):
#   return n**2
# l1=eval(input("enter any"))
# x=map(sqr,l1)
# print(list(x))
#======================
# def sqr(n):
#   return n+5
# l1=eval(input("enter any"))
# x=map(sqr,l1)
# print(list(x))

#===================aadd multiple list base on position
def add(x,y,z):
    return x+y+z
l1=eval(input("enter any"))
l2=eval(input("enter any"))
l3=eval(input("enter any"))
p=tuple(map(add,l1,l2,l3))#loop two time
print(p)
#map function take multiple list or element 