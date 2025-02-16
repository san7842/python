# def add(x,y,z):
#     "for adding of 3 variable"
#     return x+y+z
# p=int(input("enter any number"))
# q=int(input("enter any number"))
# r=int(input("enter any number"))
# res=add(p,q,r)
# print(res)
# print(add.__doc__)
# def add(x,y,z):
#     "for adding of 3 variable"
#     x+y+z
# p=int(input("enter any number"))
# q=int(input("enter any number"))
# r=int(input("enter any number"))
# res=add(p,q,r)
# print(res)
# print(add.__doc__)
# def mult(x,y,z):
#     "multiplication of two number"
#     return x*y*z
# p=int(input("enter any number"))
# q=int(input("enter any number"))
# r=int(input("enter any number"))
# res=mult(p,q,r)
# print(res)
#=====position argument=======
# def add(x,y,z):
#     print("x:",x)
#     print("y:",y)
#     print("z:",z)
#     return x+y+z
# p=int(input("enter any number"))
# q=int(input("enter any number"))
# r=int(input("enter any number"))
# res=add(p,q,r)
# print(res)
#==============key value argument====
# def add(x,y,z):
#     print("x:",x)
#     print("y:",y)
#     print("z:",z)
#     return x+y+z
# p=int(input("enter any number"))
# q=int(input("enter any number"))
# r=int(input("enter any number"))
# res=add(z=p,y=q,x=r)
# print(res)
#===============default  argument===
# def add(x=0,y=0,z=0):
#     print("x:",x)
#     print("y:",y)
#     print("z:",z)
#     return x+y+z
# p=int(input("enter any number"))
# q=int(input("enter any number"))
# r=int(input("enter any number"))
# res=add()
# print(res)
#variable-length position argument
# def add(*n):#(single * args) args as a tuple value hold
#     print(n)
#     print(type(n))
   
    

# res=add(2,4,8,67)
# print(res)
# def add(*args):
#    sum=0
#    for i in args:
#     sum+=i
#    return sum

# res=add(2,4,6,8,9,10)
# print(res)
# n=eval(input("enter any number"))
# print(n)
# print(type(n))
# def add(*args):
#     sum=0
#     for i in args:
#         for j in i:
#             sum+=j
#     return sum
# n=eval(input("enter any number"))
# res=add(n)
# print(res)

#======================
# def add(*args):
#     sum=0
#     for i in args:
#         for j in i:
#             sum+=j
#     return sum
# n=eval(input("enter any number"))
# res=add(*n)
# print(res)

#==================
def add(*args):
    "add multiple element"
    sum=0
    for i in args:
        sum+=i
    return sum
x=eval(input("enter two or more element"))
res=add(*x)
print(res)