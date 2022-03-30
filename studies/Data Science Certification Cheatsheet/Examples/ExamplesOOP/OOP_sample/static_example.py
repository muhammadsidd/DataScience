"""
Created on Jun 22, 2017

@author: SummitWorks
"""


class Car(object):
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def make_car_sound():
        print('VRooooommmm!')


mustang = Car('Ford', 'Mustang')
print(mustang.wheels)
#
# print(Car.wheels)
#
# Car.make_car_sound()
