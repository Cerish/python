#直接使用type 获得类型
import types
print(type(123))
def fn(): 
    pass
print(type(fn) == types.FunctionType)

#使用isinstance
a = 3
b = {}
c = []
d = ()
print(isinstance(a, int))
print(isinstance(b, dict))
print(isinstance(c, list))
print(isinstance(d, tuple))

#使用dir 
d = ('name', 'age','score')
print(dir('d'))
print(d.__len__())

#getattr()、setattr()以及hasattr()
class Student(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x**2
stu = Student()
print(hasattr(stu, 'x'))
print(hasattr(stu, 'y'))

print(getattr(stu, 'x'))

print(getattr(stu, 'Y',12))
setattr(stu, 'Y', 18)
print(getattr(stu, 'Y'))