# def first():
#     return "hello"
# x=first()
# print(x)
# def first():
#     yield "hello"
# x=first()
# print(x)
# def first():
#     yield 1
#     yield 2
#     yield 3
# x=first()
# print(x)
# print(list(x))
# def first():
#     yield 1
#     yield 2
#     yield 3
# x=first()
# print(next(x))
# print("hi")
# print("hello")
# print("welcome")
# print(next(x))
def natural(x):
    i=1
    while i<=x:
        yield i
        i=i+1
n=int(input("enter any number"))  
x=natural(n)
print(x)
print(list(x))
print(next(x))
print(next(x))
for i in x:
    print(i)
