'''
Created on Jan 25, 2018

@author: SummitWorks
'''
import cx_Oracle
con = cx_Oracle.connect("system", "root12", "localhost/xe")
print("db conneted")
cur = con.cursor()

print("Database version:", con.version)
cur.execute("select name,salary from employee")
res = cur.fetchall()

print('Array indexes:')
for row in res:
    print(row[0], "->", row[1])

print('Loop target variables:')
for c1, c2 in res:
    print(c1, "->", c2)  # CRUD Operation

con.close()