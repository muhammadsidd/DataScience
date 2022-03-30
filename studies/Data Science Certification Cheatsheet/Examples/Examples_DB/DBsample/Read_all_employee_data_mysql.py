import pymysql

# Open database connection
dbconn = pymysql.connect(host="localhost",
                         user="root",
                         password="root",
                         database="python_mysql")
cursor = dbconn.cursor()

query = ("SELECT * FROM employee")

cursor.execute(query)

for (empid, empfname, emplname, empage,empGender, salary) in cursor:
    print("{}, {}, {}, {},{}".format(empid, empfname, emplname, empage, empGender, salary))

cursor.close()
dbconn.close()