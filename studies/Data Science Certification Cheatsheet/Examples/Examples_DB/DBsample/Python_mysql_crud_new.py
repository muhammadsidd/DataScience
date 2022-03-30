'''
Created on Aug 8, 2017

@author: SummitWorks
'''
import pymysql


# Function create Table for initialize system of step zero!
def createTable():
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # Create table as per requirement
    sqlCreateTable = """CREATE TABLE EMPLOYEE (
    ID INT NOT NULL AUTO_INCREMENT,
    FIRST_NAME  CHAR(20) NOT NULL,
    LAST_NAME  CHAR(20),
    AGE INT,  
    SEX CHAR(1),
    INCOME FLOAT,
    PRIMARY KEY(ID))"""

    # Execute the SQL command
    cursor.execute(sqlCreateTable)
    # Commit your changes in the database
    db.commit()
    return "Employee table created successfully\n"


# Function insert record
def insert():
    fname = input("Enter the name:\n")  # django forms to generate forms and read data from the form
    lname = input("Enter the surname:\n")
    age = input("Enter the age:\n")
    age = int(age)
    sex = input("Enter gender (M / F):\n")
    income = input("Enter the income:\n")
    income = float(income)

    # Prepare SQL query to INSERT a record into the database.
    sqlInsert = """INSERT INTO EMPLOYEE(FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES ('%s','%s', '%d', '%c', '%.2d')""" % (fname, lname, age, sex, income)

    # Execute the SQL command
    cursor.execute(sqlInsert)
    # Commit your changes in the database
    db.commit()

    return print("Saved successfully!\n")


# Function list all records of employee
def selectAll():
    sqlSelectAll = "SELECT ID, FIRST_NAME, LAST_NAME, AGE, SEX, INCOME FROM EMPLOYEE"

    # Execute the SQL command
    cursor.execute(sqlSelectAll)

    print("List of registered employees:\n")

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    print(results)
    for row in results:
        id = row[0]
        fname = row[1]
        lname = row[2]
        age = row[3]
        sex = row[4]
        income = row[5]
        # Now print fetched result
        print("id = %d,fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
              (id, fname, lname, age, sex, income))


def selectById(id):
    # Prepare SQL query to SELECT all records of EMPLOYEE table when ID = ?.
    selectById = "SELECT * FROM EMPLOYEE WHERE id = '%d'" % (id)

    # Execute the SQL command
    cursor.execute(selectById)

    # Fetch all the rows in a list of lists.
    results = cursor.fetcone()

    if results is None:
        print("There is no one registered with this ID!")

    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # Now print fetched result
        return print("fname = %s,lname = %s,age = %d,sex = %s,income = %d" %
                     (fname, lname, age, sex, income))


# Function change an record
def update():
    id = input("Enter the user id to change the registration:\n")
    id = int(id)

    fname = input("Enter the name:\n")
    lname = input("Enter the surname:\n")
    age = input("Enter the age:\n")
    age = int(age)
    sex = input("Enter gender (M / F):\n")
    income = input("Enter the income:\n")
    income = float(income)

    # Prepare SQL query to UPDATE a record into the database.
    sqlInsert = """UPDATE EMPLOYEE SET FIRST_NAME = '%s',
    LAST_NAME = '%s', AGE = '%d', SEX = '%c', INCOME = '%.2d'
    WHERE ID = '%d'""" % (fname, lname, age, sex, income, id)

    # Execute the SQL command
    cursor.execute(sqlInsert)
    # Commit your changes in the database
    db.commit()

    return print("Changed successfully!\n")


# Function remove record
def delete():
    id = input("Enter the user id to remove it from the system:\n")
    id = int(id)

    # Prepare SQL query to DELETE a record when ID = ?
    sqlDelete = """DELETE FROM EMPLOYEE WHERE ID = '%d'""" % (id)

    # Execute the SQL command
    cursor.execute(sqlDelete)
    # Commit your changes in the database
    db.commit()

    return print("Removed successfully!")


# Function to continue or stop
def proceed(confirm):
    if confirm == "y":
        opc = 0
    else:
        opc = 5


############# END OF FUNCTIONS ######################

# Open database connection
db = pymysql.connect(host="localhost",
                         user="root",
                         password="root",
                         database="python_mysql")

# prepare a cursor object using cursor() method
cursor = db.cursor()

print("\n------------- Employee Control System Menu ------------\n");
opc = int(0)

try:

    # Function create Table
    # Function for initialize system of step zero!
    # createTable()

    while opc != 5:
        opc = input(
            "Choose only one of the options: \n 1-New employee registration \n 2-List registered employees \n 3-Change a registered employee \n 4-Remove a registered employee \n 5-Exit the system\n")
        opc = int(opc)

        if opc == 1:
            # Function insert record
            insert()

        elif opc == 2:
            # Function list all records of employee
            selectAll()

        elif opc == 3:
            # Function change an record
            update()
            selectAll()

        elif opc == 4:
            # Function remove record
            delete()
            selectAll()

        elif opc == 5:
            print("You left the system...")

        else:
            print("\nInvalid option!\n")

except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
