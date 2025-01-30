# l=[10,20,30,40,"sandeep"]
# print(l)
# print(type(l))
# l=["sandeep","Anil","arvind"]
# print(max(l))
# l=["sandeep","Anil",12,13]
# print(max(l))
# l1=[10,20,30,"hello"]
# print(len(l1))
# l1=[10,20,30,40]
# print(sum(l1))
# l2=[10,20,30.40,"hello"]
# print(sum(l2))#type error operand type(s)+:'float ' and 'str'
# l2=[10,20,30,40.5]
# print(sum(l2))
# l=[10,20,30,40.5,"hello"]
# l.append(78)
# print(l) 
# l.append([10,20,30,40])
# print(l)
# l.extend([10,20,30])
# print(l)
# # l.insert(0,"sand")
# # print(l)
# # l.insert("sand",0)#str object cannot be interpreter as an integer
# print(l.pop())
# print(l)
# l.remove("hello")
# print(l)
# l=[10,20,30,40,10]
# l.remove(10,2)#remove take one argument
# print(l)
#l=[10,20,30,40,10]
# l1=l.clear()
# print(l)
# print(type(l))
# del l
# print(l)
#copy
# l=[10,20,30,40,10]
# l1=l.copy()
# print(l)
# print(l1)
# print(id(l),id(l1))

#count
# l=[10,20,30,40,10]
# l1=l.count(10)
# print(l1)

#index
# l=[10,20,30,40,10,20,90]
# print(l.index(10,5))

#reverse
# l=[10,20,30,40,10]
# l.reverse()
# print(l)
# l.sort()
# print(l)

#l.sort(reverse=true)decending order
l=[10,20,30,40,10]
l.sort(reverse=True)
print(l)
 