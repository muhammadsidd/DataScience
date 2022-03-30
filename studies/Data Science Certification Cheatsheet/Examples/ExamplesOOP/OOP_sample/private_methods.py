"""
Created on Jun 22, 2017

@author: SummitWorks
"""


class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')
        self.__updateSoftware()

    def __updateSoftware(self):
        print('updating software')


redcar = Car()
redcar.drive()
redcar.__updateSoftware()  # not accesible from object.
# Encapsulation prevents from accessing accidentally, but not intentionally.
