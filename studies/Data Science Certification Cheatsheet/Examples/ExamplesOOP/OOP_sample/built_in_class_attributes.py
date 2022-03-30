"""
Created on Aug 1, 2017

@author: SummitWorks
"""


class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayCount()

# calling a method with a list of n arguments is equivalent to
# calling the corresponding function with an argument list that is
# created by inserting the method’s instance object before the first argument.
# Same as emp2.displayEmployee()
# Employee.displayEmployee(emp2)


# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)
