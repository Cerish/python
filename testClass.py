class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_age(self):
        print('%s %s' % (self.name, self.age))
    def get_grade(self):
        if self.age > 20:
            return '2000年前生的'
        elif self.age > 10:
            return '2010年前生的'
        else:
            return '2010年后生的'

li = Student('lihua', 1)
wang = Student('wangwu', 55)
zhang = Student('zhangsan', 5)

print(li.name, li.get_grade())
print(wang.name, wang.get_grade())
print(zhang.name, zhang.get_grade())

print(Student)