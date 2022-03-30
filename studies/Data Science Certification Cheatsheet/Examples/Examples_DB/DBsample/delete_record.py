import pymysql
# Open database connection
dbconn = pymysql.connect(host="localhost",
                         user="root",
                         password="root",
                         database="python_mysql")

# prepare a cursor object using cursor() method
cursor = dbconn.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE5 WHERE AGE > '%d'" % (20)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    dbconn.commit()
except:
    # Rollback in case there is any error
    dbconn.rollback()

print("data deleted..")
# disconnect from server
dbconn.close()