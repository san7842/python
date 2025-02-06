# n=int (input("enter any number"))
# if(n%2==0):
#     print(f'{n} even no')
# else:
#     print(f'{n} odd no')

# print("hello")
# age=int(input("enter your age"))
# if(age>=18):
#     print("eligible for vote")
# else:
#     print("not eligible for vote")
n=int(input("enter any percentage"))
if n>=100:
    print("please enter valid no:")
else:
    if(n>=60):
        print(f'{n} is 1st division')
    elif(n<60 and n>=45):
        print(f'{n} is 2nd division')
    elif(n<45 and n>=35):
        print(f'{n} is 3rd division')
    else:
        print(f'{n} fail')
