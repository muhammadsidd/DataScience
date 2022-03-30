'''
Created on Apr 26, 2018

@author: SummitWorks
'''
import pymysql
from pymysql import Error
try:
        con = pymysql.connect("localhost","root","root","jdbcprog" )
        print('Connected to MySQL database')
        curso = con.cursor()
        curso.callproc('getAllRecords')
#         row = curso.fetchone ()
#         print(row)
        data = curso.fetchall ()
        for row in data :
            print(row)

#         for result in curso.stored_results():
#             print(result.fetchall())
except Error as e:
        print(e)

finally:
        con.close()
        