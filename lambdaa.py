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
x=int(input("enter any"))
res=lambda x:[i for i in range(1,x) for k in range(x)]
print(res(x))