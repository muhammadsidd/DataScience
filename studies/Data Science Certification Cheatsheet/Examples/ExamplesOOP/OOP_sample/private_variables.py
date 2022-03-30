"""
Created on Jun 22, 2017

@author: SummitWorks
"""


class Car:
    __maxspeed = 0
    _name = ""

    def __init__(self):
        self.__maxspeed = 200
        self._name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))


redcar = Car()
redcar.drive()
print(redcar._name)

# redcar.__maxspeed = 10  # will not change variable because its private
# redcar._name = 'NewRedCar'
# redcar.drive()
# print(redcar._name)


