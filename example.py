#============example 1===========
# n=int(input("enter any number"))
# if(n>0):
#     print(f'{n} is positive')

#==========example2========
# n=int(input("enter any number"))
# if(n>0):
#     print(f'{n} is positive')
# else:
#      print(f'{n} is negative')
#===========================
# n=int(input("enter any number"))
# if(n>0):
#     print(f'{n} is positive')
# elif(n<0):
#     print(f'{n} is negative')
# else:
#     print(f'{n} is zero')
#===========swaping=========
# m=eval(input("enter any "))
# n=eval(input("enter any "))
# m,n=n,m
# print(m)
# print(n)
#=========================
# n=int(input("enter any number"))
# sqr=n**0.5
# print("square root",sqr)
#=============cube root===========
# n=int(input("enter any number"))
# sqr=n**(1/3)
# print("cube root",sqr)
#======================
# x=int(input("enter any number"))
# y=int(input("enter any number"))
# z=int(input("enter any number"))
# if(x>y and x>z):
#     print(f'{x} is greater')
# elif(y>x and y>z):
#     print(f'{y} is greater')
# else:
#     print(f'{z} is greater')
#==========================
# hieght=int(input("enter hieght"))
# base=int(input("enter base"))
# area=(hieght*base)/2
# print(area)
#====area of square=====
# n=int(input("enter any length"))
# area_of_square=n*n
# print(area_of_square)
#===========leap or non leap year=====
# year=int(input("enter year"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print(f'{year} is leap year')
# else:
#     print(f'{year} is not leap year')
#===leap year or not leap year=====
# year=int(input("enter any year"))
# if(year%4==0):
#     if(year%100==0):
#         if(year%400==0):
#             print(f'{year} is leap year')
#         else:
#             print(f'{year} is not leap year')
#     else:
#         print(f'{year} is leap year')
# else:
#     print(f'{year}is not leap yera')
#=====while loop===========
#======n natural number============
# n=int(input("enter any number"))
# i=1
# while(i<=n):
#     if(i<n):
#      print(i,end=",")
#     else:
#        print(i)
#     i+=1
#========
# n=int(input("enter any number"))
# sum=0
# i=1
# while(i<=n):
#     if(i<n):
#      print(i,end=",")
#      sum+=i
#     else:
#        print(i)
#        sum+=i
#     i+=1
# print("sum",sum)
#==========even number=========
# n=int(input("enter any number"))
# i=1
# while(i<=n):
#     if(i%2==0):
#         if(i<n):
#             print(i,end=",")
#         else:
#             print(i)
#     i+=1
#=================odd number=======
# n=int(input("enter any number"))
# i=1
# while(i<=n):
#     if(i%2!=0):
#         if(i<n):
#             print(i,end=",")
#         else:
#             print(i)
#     i+=1
#=================factorial========
# n=int(input("enter any number"))
# f=1
# i=1
# while(i<=n):
#     f*=i
#     i+=1
# print("facatorial",f) 
#==================ten time name==========
# n=int(input("enter any number"))
# i=1
# while(i<=n):
#     print("sandeep")
#     i+=1
#============vowels and consonant====
# n=input("enter word")
# vol=0
# const=0
# i=0
# while(i<len(n)):
#     x=( 'A','E','I','O','U','a','e','i','o','u')
#     y=n[i]
#     if(y in x):
#         vol+=1
#     else:
#         const+=1
#     i+=1
# print('vol:',vol,'const:',const)
#===================
# l=[10,20,30,40,50]
# a=len(l)
# i=0
# while(i<a):
#     print(l[i]+5)
#     i+=1
#=====================
# t=(10,20,30,40,50)
# a=len(t)
# i=0
# while(i<a):
#     print(t[i]+5)
#     i+=1
#=================
# s1="sandeep"
# a=len(s1)
# l=[]
# i=0
# while(i<a):
#    l.append(s1[i])
#    i+=1
# print(l)
#============================


# n=int(input("enter any number"))
# for i in range(1,n+1):
#     if(i<n):
#      print(i ,end=",")
#     else:
#        print(i)
#==============================
# n=int(input("enter any number"))
# for i in range(1,n+1):
#     if(i%2==0):
#         print(i,end=" ")
    
#=====================
# n=int(input("enter any number"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum",sum)
#============================
# n=int(input("enter any number"))
# sum=0
# for i in range(1,n+1):
#     if(i%2!=0):
#      print(i,end=" ")
#      sum+=i

# print("sum:",sum)
#========================table=======
# n=int(input("enter any number"))
# for i in range(1,11):
#     print(i*n)
#===============================

# l=[]
# for i in l:
#     l1=l.append(i)
#     print(l1)
#==========================
# l=[1,2,7,4,5,6]
# for i in l:
#     print(i)

#==========================
# n=int(input("enter number"))
# n1=str(n)
# count=0
# for i in n1:
#     count+=1
# print(count)
#===================amstrong=============
# n=int(input("enter any number"))
# x=n
# y=n
# digit=0
# sum=0
# while n>0:
#     n=n//10
#     digit+=1
# while x>0:
#     last_digit=x%10
#     sum+=last_digit**digit
#     x=x//10
# if(sum==y):
#     print("armstrong")
# else:
#     print("not armstrong")
#==================reverse====================
# str=eval(input("enter any"))
# rev=""
# for i in str:
#     rev=i+rev
# print("rev:",rev)
#==============palindrome======
# str=(input("enter any number"))
# a=str
# b=str[: :-1]
# if(b==a):
#     print(f'{a} is palindrome')
# else:
#     print(f'{a}is not palindrome')
#=========================
# str=(input("enter any number"))
# a=str
# rev=""
# for i in str:
#     rev=i+rev
# if(rev==a):
#     print(f'{a} is palindrome')
# else:
#     print(f'{a}is not palindrome')

#==============series==even or odd=========
# n=eval(input("enter any series"))
# even=0
# odd=0
# for i in n:
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# print("even",even)
# print("odd",odd)
#=========================
# n=eval(input("enter any series"))
# for i in n:
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# print("even",even)
# print("odd",odd)
        
#=======================except prime no===========
# l=eval(input("enter any"))
# for i in range(l+1):
#     if(i>1):
#         for j in range(2,i):
#             if(i%j==0):
#              print(i,end=" ")
#              break
#=====fibonaci================
# n=int(input("enter any number"))
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(2,n+1):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
            
#========factorial===========
# n=int(input("enter any number"))
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)

# n=int(input("enter any number"))
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(1,n+1):
#    c=a+b
#    print(c,end=" ")
#    a=b
#    b=c
# n=int(input("enter any"))
# x=n
# y=n
# sum=0
# dig=0
# while n>0:
#     n=n//10
#     dig+=1
    
# while(x>0):
#    last_dig=x%10
#    sum+=last_dig**dig
#    x=x//10
# if(sum==y):
#     print("armstrong")
# else:
#     print("not a armstrong")

# n=(input("enter any"))
# rev=""
# for i in n:
#     rev=i+rev
# if(rev==n):
#     print("palindrome")
# else:
#     print("not a palindrome")
# n=int(input("enter any"))
# a=n
# rev=""
# while n>0:
#     last_dig=n%10
#     rev=rev*10+last_dig
#     n=n//10
# if(rev==a):
#     print("palind")
# else:
#     print("not palind")
# n=15
# a=0
# b=1
# while a<=n:
#     print(a)
#     a,b=b,a+b
#================== 
# s1=input("enter any ")
# l1=[]
# for i in s1:
#     x=ord(i)
#     l1.append(x)
#     y=(65-90 and 97-122 and 48-57 and 58-64)
#     if(x in y):
#         print("strong")
#     else:
#         print("not ")
#======================================
# n=(input("enter any "))
# x=n
# rev=""
# for i in n:
#     rev=i+rev
# if(rev==x):
#     print("palindrome")
# else:
#     print("not palindrome")
#==================
# n=int(input("enter any number"))
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(1,n+1):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
#===============================
n=int(input("enter any number"))
a=0
b=1
while(a<=n):
    print(a,end=" ")
    a,b=b,a+b
