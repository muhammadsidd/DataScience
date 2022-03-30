'''
Created on Jun 22, 2017

@author: SummitWorks
'''


#
# import datetime
# today = datetime.datetime.now()
# #When I use the built-in function str() to display today:
# print(str(today))	#'2018-01-12 09:21:58.130922‘
# print(repr(today))	#'datetime.datetime(2018, 1, 12, 9, 21, 58, 130922)'


class Animal:
    # static variables
    def __init__(self, name=''):
        self.name = name

    def talk(self):
        pass


class Cat(Animal):
    def talk(self):  # function overriding, if they have same f name and same number of arguments.
        print("Meow!")
        print(self.name)

    def __str__(self):
        return "the name of the cat is " + self.name
        # print("the name of the cat is " , self.name)

    @staticmethod
    def one():
        print("its a static method")


class Dog(Animal):
    def talk(self):
        print("Woof!")
        print(self.name)

    def __str__(self):
        return "the name of the Dog is " + self.name


a = Animal()
a.talk()

c = Cat("Missy")
c.talk()
# c.one()
d = Dog("Rocky")
d.talk()

d1 = Dog()
d.talk()

print(c)
print(d)
Cat.one()
