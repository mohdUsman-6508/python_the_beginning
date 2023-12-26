# one class can inherit methods of another class(parent class)

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def mew(self):
        print("mew")


tommy=Dog()
tommy.walk()
tommy.bark()

blacky=Cat()
blacky.walk()
blacky.mew()

