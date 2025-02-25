# def even(n):
#     if n%2==0:
#         return n
# l1=eval(input("enter any"))
# x=(filter(even,l1))
# print(list(x))
# def even(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 break
#             return n
# l1=eval(input("enter any"))
# x=(filter(even,l1))
# print(list(x))
#======================
def prime(n):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
            return n
l=eval(input("enter any"))
p=filter(prime,l)
print(list(p))