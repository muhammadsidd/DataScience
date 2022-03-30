from pymongo import MongoClient


def main():
    while 1:
        # choosing a  option to do CRUD operations
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print
            '\n INVALID SELECTION \n'


client = MongoClient('localhost:27017')
db = client.EmployeeData


# Function to insert data into mongo db
def insert():
    # creating connectioons for communicating with Mongo DB
    client = MongoClient('localhost:27017')
    db = client.EmployeeData
    try:
        employeeId = input('Enter Employee id :')
        employeeName = input('Enter Name :')
        employeeAge = input('Enter age :')
        employeeCountry = input('Enter Country :')

        db.Employees.insert_one(
            {
                "id": employeeId,
                "name": employeeName,
                "age": employeeAge,
                "country": employeeCountry
            })
        print('\nInserted data successfully\n')

    except Exception:
        print("Exception while inserting a record")


# function to read records from mongo db
def read():
    try:
        empCol = db.Employees.find()
        print('\n All data from EmployeeData Database \n')# [(),()]
        for emp in empCol:
            print(emp)

    except Exception:
        print("Exception while reading a record")


def update():
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')

        db.Employees.update_one(
            {"id": criteria},
            {
                "$set": {
                    "name": name,
                    "age": age,
                    "country": country
                }
            }
        )
        print("\nRecords updated successfully\n")

    except Exception:
        print("Exception while reading a record")


# Function to delete record from mongo db
def delete():
    try:
        criteria = input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id": criteria})
        print('\nDeletion successful\n')
    except Exception:
        print("Exception while deleting a record")


main()
