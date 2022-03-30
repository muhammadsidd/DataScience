"""
Created on Jun 22, 2017

@author: SummitWorks
"""


class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    # overriding
    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


a = Animal()
a.whoAmI()

# d = Dog()
# d.whoAmI()
# d.bark()
