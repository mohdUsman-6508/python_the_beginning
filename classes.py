# classes -- it is a blueprint,it helps us to define new types
# objects are the instances of a class
# each instance is independent of another
# PascalCase


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} can talk')

person1=Person('osman')
person1.name='usman'
person1.talk()

person2=Person('sahil')
person2.talk()

