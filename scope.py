
#x=10#global variable
# def new():
#     y=20
#     print(x)
#     print(y)
# new()
# print(x)
# print(y)
# x=10
# def update(p):
#     global x
#     x=p
#     print(x)
# print("before update call",x)   
# x=int(input("enter any number"))
# update(x)
# print(" after update call:",x)

#same name of local and global variable tab local me global ko access karne ke liye globals method 
x=10
def update(p):
    global x
    x=p
    print('before update :',globals()['x'])
y=int(input("enter any number"))
print("before update call",x)   

update(y)
print(" after update call:",x)



#local variable ko global variable me badal sakte hai