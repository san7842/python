# class First:
#     x=10
#     def new():
#         print("hello")
# obj=First
# print(obj.x)
# obj.new()
# class First:
#     x=10
#     def new():
#         print("hello")
# obj=First
# print(obj.x)
#obj.new()
#print(dir(First))
#'''['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__',
 #'__format__', '__ge__', '__getattribute__', '__getstate__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 #  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', 
 #  '__str__', '__subclasshook__', '__weakref__', 'new', 'x']'''
# class Student:
#     def __init__(self):
#         print("this is constructor")
#     def display(self):
#         print("hello")
# obj=Student
# obj.display()
class Student:
    def __init__(self):
        print("this is constructor")
        print(id(self))
    def display(self):
        print("hello")
#obj=Student
#obj.display()
obj=Student()
print(id(obj))
#obj.display()