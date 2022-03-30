class Person(object):

    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return  self.name +" member of "+Person.__name__

class Student(Person):

    status_const = ''

    def __init__(self,name, address, phone, email, status):
        super().__init__(name, address, phone, email)
        status_const = status

    def __repr__(self):
        return  self.name +" member of "+Student.__name__

class Employee(Person):

    def __init__(self, name, address, phone, email, office, salary, date_hired):
        super().__init__(name, address, phone, email)
        self.office = office
        self.salary = salary
        self.date_hired = date_hired

    def __repr__(self):
        return  self.name +" member of "+Employee.__name__

class Faculty(Employee):

    def __init__(self, name, address, phone, email, office, salary, date_hired, office_hours, rank):
        super().__init__(name, address, phone, email, office, salary, date_hired)
        self.office_hours = office_hours
        self.rank = rank

    def __repr__(self):
        return  self.name +" member of "+Faculty.__name__

class Staff(Employee):

    def __init__(self, name, address, phone, email, office, salary, date_hired, title):
        super().__init__(name, address, phone, email, office, salary, date_hired)
        self.title = title

    def __repr__(self):
        return  self.name +" member of "+Staff.__name__

def gen (attribute):

    i = 0
    while i < len(attribute):
        yield attribute[i]
        i+=1

def print_generated_values(a):
    p = gen(my_dict[a])
    for i in range(0, len(my_dict[a])):
        yield p[i]



a = Person('Chandler Bing ', '7111 68th Drive East Bradenton Fl 34203', 2021234567, 'chandler@friends.com')
b = Person('Monica Galler', '311 Block 4 manhattan New York, NYC 90210', 4081234567, 'Monica@friends.com')
c = Student('Joey Tribiani', '404 Boulevard Manhattan New York, NYC, 90211', 5412345678, 'joey@friends.edu', 'Junior')
d = Student('Racheal Green', '623 Brooklyn Dr Ney York, NYC, 90222', 6341238901, 'racheal@friends.edu', 'freshmen')
e = Student('Phoebe Buffet', '666 Brooklyn Dr Ney York, NYC, 90222', 6342238209, 'phoebe@friends.edu', 'senior')
f = Faculty('Jerry Seinfeld', '5020 Bordeaux Village Pl Tampa Fl 33617', 2696784567, 'seinfeld@seinfeldtv.com', 'Block 9', 4500, 'dec 1994', '8:00 am - 10:00 am', 'Director')
g = Faculty('George Costanza', '2610 Rustic Ridge Loop Lutz Fl 33559', 2696782568, 'george@seinfeldtv.com', 'Block 8', 3500, 'jan 1995', '9:00 am - 10:00 am', 'Manager')
h = Staff('Eleine Bennet', '2511 Rustic Ridge Grove lutz Fl, 33552', 7234561234, 'eleine@seinfeldtv.com', 'Block 2', 2300, 'march 1995', 'Editor')
k = Staff('Kramer  Cosmo', '4140 East Fowler Avenue Tampa Fl, 33620', 3233561333, 'kramer@seinfeldtv.com', 'Block 1', 4300, 'April 1995', 'Neighbor')
l = Employee('Jon snow', '3334 Westfield blvd Orlando, Fl, 38918', 4129803451, 'jonsnow@got.com', 'KingsLanding', 8000, 'June 2010')
m = Employee('Denyrs Targayren', '4908 bayshore Gardens Orlando, Fl, 38898', 4695895221, 'chains@got.com', 'Dragonstone', 10000, 'May 2010')
n = Employee('Sansa Stark', '1234 Tara blvd sarasota, Fl, 38918', 5129303451, 'ladysansa@got.com', 'Winterfell', 12000, 'June 2011')
o = Employee('Arya Stark', '456 Blindlane ally Venice, Fl, 38942', 34481343451, 'knightkiller@got.com', 'Bravos', 8000, 'June 2010')
p = Employee('Harry Potter', '786 Muggleville Melbourne, Fl, 34321', 4042116851, 'dumbledorsbaby@hogsward.com', 'Diagon ally', 8000, 'June 2003')

my_dict = {'Person':[a,b], 'Student':[c,d,e], 'Faculty':[f,g], 'Staff':[h,k], 'Employee': [l,m,n,o,p]}

print("GENERATING THE DICTIONARY")
user= input("Please enter the key you wish to generate? Choice should include Person, Student, Faculty, Staff or Employee ")
print_generated_values(user.title())
