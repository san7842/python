n=int(input("enter any"))
x=n
y=n
sum=0
dig=0
while n>0:
    n=n//10
    dig+=1
    
while(x>0):
   last_dig=x%10
   sum+=last_dig**dig
   x=x//10
if(sum==y):
    print("armstrong")
else:
    print("not a armstrong")
