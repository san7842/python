# x=int(input("enter any"))
# y=int(input("enter any"))
# res=lambda p,q:(p+q)
# print(res(x,y))
# x=int(input("enter any"))
# y=int(input("enter any"))
# res=lambda p,q:print(p+q)
# print(res(x,y))
# x=int(input("enter any"))
# y=int(input("enter any"))
# res=lambda p,q:print(p+q)
# (res(x,y))
# x=int(input("enter any"))
# res=lambda y:"even"if(y%2==0) else 'odd'
# print(res(x))

# n=int(input("enter any "))
# l=[]
# for i in range(n):
#     x=int(input("enter any"))
#     l.append(x)
# print(l)
# l1=[]
# for i in range(1,4):
#     l1.append(i)
# l2=[]
# for i in range(4):
#     l2.append(l1)
# print(l2)
#lambda with for loop
#lambda x:[i for i in collection]/collection(list,tuple,string)
# x="sandeep"
# res=lambda x:[i for i in x]
# print(res(x))
# x=int(input("enter any"))
# res=lambda x:[[i for i in range(1,x)] for k in range(x)]
# print(res(x))
#=====without i in for loop===
# for _ in range(4):
#     print("hello")
# l1=eval(input("enter any"))
# x=list(map(lambda x:x**2,l1))
# print(x)
#==============map with lambda and if else======
# l1=eval(input("enter any"))
# x=list(map(lambda x:"even" if x%2==0 else "odd",l1))
# print(x)
# l1=eval(input("enter any"))
# x=list(filter(lambda x:x if x%2==0 else None,l1))
# print(x)
#================odd==========
# l1=eval(input("enter any"))
# x=list(filter(lambda x:x if x%2!=0 else None,l1))
# print(x)
#from functools import reduce
# l1=eval(input("enter any"))
# x=reduce(lambda x,y:x if x>y else y,l1)
# print(x)
#  =====min======
# l1=eval(input("enter any"))
# x=reduce(lambda x,y:x if x<y else y,l1)
# print(x)
# l1=eval(input("enter any"))
# x=reduce(lambda x,y:x+y,l1)
# print(x)

x=lambda p:[i for i in range(1,p+1)]
print(x(10))
