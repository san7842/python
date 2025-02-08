# x=int(input("enter number"))
# y=int(input("enter number"))
# z=int(input("enter number"))
# p=max(x,y,z)
# while(True):
#     if p%x==0 and p%y==0 and p%z==0:
#         break
#     p+=1
# print(f'lcm of{x},{y} and {z} is {p}')
# x=int(input("enter number"))
# y=int(input("enter number"))
# z=int(input("enter number"))
# q=p=max(x,y,z)
# i=1
# while(True):
#     if q%x==0 and q%y==0 and q%z==0:
#         break
#     i+=1
#     q=p*i
# print("lcm is",q)
x=int(input("enter number"))
y=int(input("enter number"))
z=int(input("enter number"))
p=min(x,y,z)
q=1
i=2
while(i<p):
    if x%i==0 and y%i==0 and z%i==0:
        q*=i
    i+=1
print("hcf is",q)