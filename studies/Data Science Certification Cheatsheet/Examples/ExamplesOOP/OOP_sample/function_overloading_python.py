"""
Created on Aug 4, 2017

@author: SummitWorks
"""


class Test:
    def add(self, instanceOf, *args):  # really not overloaded.
        if instanceOf == 'int':
            result = 0
        if instanceOf == 'str':
            result = ''
        for i in args:
            result = result + i
        return result


t1 = Test()
print(t1.add('int', 3, 4, 5))  # if f name is same and diff parameters.
print(t1.add('str', 'I', ' am', ' in', ' Python'))
