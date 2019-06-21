#多重继承 取左原则
class Animal():
    def __init__(self):
        self.name = 'Animal'

class Manmal(Animal):
    def __init__(self):
        self.name = 'Manmal'

class Bird(Animal):
    def __init__(self):
        self.name = 'Bird'

class Dog(Manmal, Animal):
    pass

class Cat(Bird, Manmal):
    pass

class Parrot(Bird, Animal):
    pass

dog = Dog()
print(dog.name)

parrot = Parrot()
print(parrot.name)

cat = Cat()
print(cat.name)

