class Animal(object):
    __slots__ = ('name', 'age')

#如果子类也定义了__slots__,那么子类允许定义的属性就是自身的__slots__和父类的__slots__
class Dog(Animal):
    __slots__ = ('mouth')

a = Animal()
dog = Dog()

a.name = 'animal'
print(a.name)

#未在__slots__中定义属性的不可添加
# a.eyes = 'blue'
# print(a.eyes)
dog.mouth = 'blue'
print(dog.mouth)