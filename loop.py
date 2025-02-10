# n=int(input("enter any number"))
# c=0
# i=0
# while(i<=n):
#      if(i<n):
#       print(i,end=",")
#      else:
#         print(i)
#      c+=1
#      i+=1
# print(c)
# print("hello",end=",")
# print()

#n=
#====even number=====
n=int(input("enter number"))
sum1=0
sum2=0
i=1
while(i<=n):
   if(i%2==0):
     if(i<n):
      print(i,end="+")
      sum1+=i
     else:
         print(i,end='=')
         sum2+=i
   i+=1
sum=sum1+sum2
print(sum)
#==== 10 even number====
# n=int(input("enter range"))
# even=0
# i=1
# while(i<=n):
#    if(i%2==0):
#        print(i,end=",")
#        even+=1
#        if(even==10):
#          break
#    i+=1
#=====odd upto 10
# n=10
# i=1
# while(i<=n):
#    if(i%2!=0):
#       if(i<n):
#        print(i,end=",")
#       else:
#          print(i)
#    i+=1




#=====odd=====    
n=int(input("enter number"))
i=1
while(i<=n):
   if(i%2!=0):
      if(i<n):
       print(i,end=",")
   i+=1
