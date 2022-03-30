"""
Created on Jul 10, 2017

@author: SummitWorks
"""
import psycopg2

conn = psycopg2.connect(database = "employees", user = "postgres", password = "root", host = "127.0.0.1", port = "5432")
print("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print("Table created successfully")

conn.commit()
conn.close()