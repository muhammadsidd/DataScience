import pymysql

# Open database connection
dbconn = pymysql.connect(host="localhost",
                         user="root",
                         password="root",
                         database="python_mysql")

# prepare a cursor object using cursor() method
cursor = dbconn.cursor()

# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > '%d'" % (1000)
sql = "SELECT * FROM EMPLOYEE"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall() #[(,,),()....]
    for row in results: #(,,,)
        id = row[0]
        fname = row[1]
        lname = row[2]
        age = row[3]
        gender = row[4]
        income = row[5]
        # Now print fetched result
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, gender, income ))
except:
    print("Error: unable to fecth data")

# disconnect from server
dbconn.close()