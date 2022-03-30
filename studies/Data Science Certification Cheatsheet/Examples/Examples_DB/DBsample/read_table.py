'''
Created on Jun 26, 2017

@author: SummitWorks
'''
import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select name, salary, department, email from test where name='Ann'
    """)

    for row in cursor.fetchall():
        name, salary, department, email = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
             name, salary, department, email))