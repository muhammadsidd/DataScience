class Person:
	def __init__(self,name,address,phoneNumber,emailAddress):
		self.name=name
		self.address=address
		self.phoneNumber=phoneNumber
		self.emailAddress=emailAddress
	def __repr__(self):
		class_name=self.__class__.__name__
		return "Class Name: "+class_name+", Person Name: "+self.name

class Student(Person):
	name="None"
	def __init__(self,status):
		self.status=status
	def __repr__(self):
		class_name=self.__class__.__name__
		return "Class Name: "+class_name+", Person Name: "+self.name

class Employee(Person):
	name="None"
	def __init__(self,office,salary,dateHired):
		self.office=office
		self.salary=salary
		self.dateHired=dateHired
	def __repr__(self):
		class_name=self.__class__.__name__
		return "Class Name: "+class_name+", Person Name: "+self.name

class Faculty(Employee):
	def __init__(self,officeHours,rank):
		self.officeHours=officeHours
		self.rank=rank
	def __repr__(self):
		class_name=self.__class__.__name__
		return "Class Name: "+class_name+", Person Name: "+self.name

class Staff(Employee):
	def __init__(self,title):
		self.title=title
	def __repr__(self):
		class_name=self.__class__.__name__
		return "Class Name: "+class_name+", Person Name: "+self.name

p=Person("Tom","123 House Drive","(123)456-7890","email@address.com")
s=Student("freshman")
e=Employee("office","$100,000","Jan. 1, 1901")
f=Faculty("5:00PM","Captain")
st=Staff("Title")
print(p)
# print s
# print e
# print f
# print st