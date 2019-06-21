#访问限制
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        self.__gender = gender

li = Student('lihua', 'male')
print(li.get_gender())
li.set_gender('female')
print(li.get_gender())

#继承yu多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
dog = Dog()
dog.run()

cat = Cat()
cat.run()
