class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Hello! My name is', self.name)


p = Person('Swaroop')
p.sayHi()
Person('Swaroop').sayHi()
