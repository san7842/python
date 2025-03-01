str=input("enter any string")
str1=str
rev=""
for i in str:
    rev=i+rev
if(rev==str1):
    print("anam")
else:
    print("not anagram")