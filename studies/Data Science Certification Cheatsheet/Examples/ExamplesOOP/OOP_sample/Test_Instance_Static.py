"""
Created on Mar 1, 2018

@author: SummitWorks
"""


class Employee1:
    empCount = 0

    def __init__(self, sal, dept, name):
        self.sal = sal
        self.dept = dept
        self.name = name

    def printvalues(self):
        print(self.sal)
        print(self.name)


e1 = Employee1(232, "Dev", "Raj")
e1.printvalues()
