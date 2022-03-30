import pymysql
from symbol import except_clause

# Open database connection
db = pymysql.connect("localhost","root","root","employee_db" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE set phone = 3333 WHERE id = '%d'" % (9)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("data is updated")
except:
    # Rollback in case there is any error
    db.rollback()
# disconnect from server
finally:
    try:
        db.close()
    except:
        print("its not cconnected")