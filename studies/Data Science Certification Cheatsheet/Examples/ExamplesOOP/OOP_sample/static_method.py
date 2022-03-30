"""
Created on Jul 24, 2017

@author: SummitWorks
"""


class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    # its not recomended to declare instance variables here...
    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def rollCall():  # this is implicitly a class method (see comments below)
        print("There are {} dogs.".format(Dog.count))
        if len(Dog.dogs) > 0 :
            print("They are:")
            for dog in Dog.dogs:
                print("  {}".format(dog))

        else:
            print('There are no dogs created yet.')


Dog.rollCall()

joey = Dog("Joey")
joey.bark(3)
Dog.rollCall()

rex = Dog("Rex")
Dog.rollCall()
