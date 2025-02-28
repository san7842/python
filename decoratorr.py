#kis function ke code ko bina change kiye huye usake internal bihavier ko chang kar deta hai
#higher order function special as argument take function and return function return
# def out_fun(new):
#     def inner_fun():
#         print("hello")

#     return inner_fun
# @out_fun
# def new():
#     pass
# new()
def out_fun(s):
    def inner_fun(p,q):
        p=p+10
        q=q+10
        r=s(p,q)
        print(r)
    return inner_fun
@out_fun
def new(x,y):
    return x+y
p=int(input("enter any"))
q=int(input("enter any"))
new(p,q)