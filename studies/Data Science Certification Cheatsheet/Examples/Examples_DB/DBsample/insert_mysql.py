import pymysql

# Open database connection
dbconn = pymysql.connect(host="localhost",
                         user="root",
                         password="root",
                         database="python_mysql")

# prepare a cursor object using cursor() method
cursor = dbconn.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO employee(FIRST_NAME,
         LAST_NAME, AGE, GENDER, INCOME)
         VALUES ('Ann', 'Tylor', 28, 'F', 5000)"""
print(sql)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    dbconn.commit()
except:
    # Rollback in case there is any error
    dbconn.rollback()
    print("we cant process your request right now")

finally:
    # disconnect from server
    dbconn.close()
    
print("data has been inserted successfully...")