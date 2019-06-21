#range从下标开始，但不包含上标

# p = int(input('ll'))
# if p > 40:
#     print(1)
# else:
#     print(5)

# a = 0
# for n in range(0,201):
#     if n % 4 != 0:
#         print(n)

# match只匹配开头， search 则是全部匹配
# import re
# str = "you who are you"
# match = re.match("you", str)
# print(match.group())
# search = re.search("you", str)
# print(search.group())

# b的值为None 因为remove执行后没有返回值
# a = [1,2,3]
#b = a.remove(a[1])
# print(a)

# pop()返回被删除的值，如有参数，则删除第 i 个值
# a = [1,2,3,4]
# b = a.pop(1)
# print(b)
# print(a)

# len()不能测试 int类型的长度  bit_length()返回 改整数转换成二进制最少所需要的位数  
# a = 5
# print(a.bit_length())

# python对大小写敏感 True 和 true 不是同一个变量
# a = 1 if True else 2
# print(a)

# test = lambda x : 1 if x > 0 else 0
# print(test(0))
# print(test(5))

# __name__ 返回模块的名称， 如为当前模块， 则范围__main__。 例： if __name__ = __main__
# class Person:
#     a = 1
#     def __init__(self):
#         pass
#     def getAge(self):
#         print(__name__)
# p = Person()
# p.getAge()

# __call__ 方法可以被 实例对象直接调用
# class A(object):
#     def __init__(self,a,b):
#         self.__a = a
#         self.__b = b
#     def myprint(self):
#         print('a=', self.__a, 'b=', self.__b)
#     def __call__(self, num):
#         print('call:', num + self.__a)
 
# a1=A(10,20)
# a1.myprint()
 
# a1(80)

# 实例对象是 最先执行的方法为 __new__(),返回一个对象后， 才执行__init__()方法
# class B(object):
#     def fn(self):
#         print('B fn')
#     def __init__(self):
#         print("B INIT")
 
# class A(object):
#     def fn(self):
#         print('A fn')
 
#     def __new__(cls,a):
#             print("NEW", a)
#             if a>10:
#                 return super(A, cls).__new__(cls)
#             return B()
 
#     def __init__(self,a):
#         print ("INIT", a)

# a1 = A(5)
# a1.fn()
# a2=A(20)
# a2.fn()

# __getattr__ 使实例对象使用类中不存在的方法时，返回 自定义 默认的方法或属性
# class A(object):
#     def __init__(self,a,b):
#         self.a1 = a
#         self.b1 = b
#         print('init')
#     def mydefault(self):
#         print('default')
#     def __getattr__(self, name):
#         print(name)
#         return self.mydefault
 
# a1 = A(10,20)
# a1.test()
# a1.fn1()
# a1.fn2()
# a1.fn3()
# a1.ksdj()

# 若使用 obj.__class__ = A 则会调用A中的方法
# class A(object):
#     def show(self):
#         print ('base show')

# class B(A):
#     def show(self):
#         print ('derived show')
 
# obj = B()
# obj.show()

# 数字、字符、元组为不可变类型，列表、字典为可变类型 （同一个数字，指向同一个id; 但同一个列表，不指向同一个id）

# multipliers()函数返回时，i为最后一个循环的数，可通过先保存i的值，来达到想要的效果
# b = [m(2) for m in multipliers()] 等同于 b = [] for m in multipliers(): b.append(m)
# def multipliers():
#     return [lambda x, i=i: i * x for i in range(4)]

# print([m(2) for m in multipliers()])

# testDict = {i: i * i for i in range(10)}

# testSet = {i * 2 for i in range(10)}

# print(testSet)

# print(testDict)

# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = [i for i in A1 if i in A0]
# A3 = [A0[s] for s in A0]
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]

# print(A0)
# print(A1)
# print(A2)
# print(A3)
# print(A4)
# print(A5)
# print(A6)

# a = [1,2,3]
# b = [4,5,6]
# zipped = zip(a,b)
# print(list(zipped))

class A(object):
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!")
    def pause(self):
        print ("wait B wait!")

class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")
    def pause(self):
        print ("wait C wait!")

class D(B, C, A):
    def go(self):
        super(D, self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    # def pause(self):
    #     print ("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# 说明下列代码的输出结果

# a.go()
# b.go()
# c.go()
# d.go()
# e.go()

# a.stop()
# b.stop()
# c.stop()
# d.stop()
# e.stop()

# a.pause()
# b.pause()
# c.pause()
d.pause()
# e.pause()