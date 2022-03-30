b'''
Created on Jun 27, 2017

@author: SummitWorks
'''
import pymysql
print('hello')
# Open database connection
db = pymysql.connect("localhost","root","root","python_mysql" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()