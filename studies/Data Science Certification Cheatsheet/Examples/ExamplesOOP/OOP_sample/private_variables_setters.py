"""
Created on Jun 22, 2017

@author: SummitWorks
"""


class Car:
    __maxspeed = 0
    _name = ""
    _test = ""
    count = 0

    def __init__(self):
        self.__maxspeed = 200
        self._name = "Supercar"
        Car.count += 1

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

    def getMaxSpeed(self):
        return self.__maxspeed


redcar = Car()
redcar.drive()

# # print(redcar.__maxspeed)
# print(redcar.getMaxSpeed())
# redcar.drive()

# # redcar.__maxspeed = 600
# redcar.setMaxSpeed(320)
# redcar.drive()



