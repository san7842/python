# s="Neeraj"
# f1=frozenset(s)
# print(f1)
# print(type(f1))
# s={10,20,30,40}
# s1={2,4,6,10,20}
s=(1,2,3,4)
s1=(1,2,3,4,5,6,7)
x=frozenset(s)
x1=frozenset(s1)
# print(x.union(x1))
# print(x.difference(x1))
# print(x.intersection(x1))
# print(x.symmetric_difference(x1))
print(x.isdisjoint(x1))
print(x.issubset(x1))
print(x1.issuperset(x))