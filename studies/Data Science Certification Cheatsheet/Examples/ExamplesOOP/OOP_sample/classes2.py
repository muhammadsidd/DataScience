class Employee:
    """Common base class for all employees"""
    empCount = 0
    family_members = 0  # its not required to declare here

    def __init__(self, name, salary, family_members):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        self.family_members = family_members;

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
        print("the number of family members of the employee are %d" % self.family_members)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
        print("Number of family members of the employee is : %d" % self.family_members)

    @staticmethod
    def static_function():
        print("its a static method")


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000, 5)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000, 4)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
emp1.displayCount()
emp2.displayCount()
Employee.static_function()
