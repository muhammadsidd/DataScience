'''
Created on Aug 1, 2017

@author: SummitWorks
'''


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # GC
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
print("Id for point 1 is {} ".format(id(pt1)))

pt2 = pt1
print("Id for point 1 is {} and point 2 is {}".format(id(pt1), id(pt2) ))

pt1.__del__()
# del pt1
print("After deleting pint 1, Id for point 2 is {} ".format(id(pt2)))

