import sqlite3
connection = sqlite3.connect("mytestdb.db")
print("database conneccted succesfully")
cursor = connection.cursor()

# delete 
#cursor.execute("""DROP TABLE employee;""")

# sql_command = """
#  CREATE TABLE employee_new123 ( 
#  staff_number INTEGER PRIMARY KEY, 
#  fname VARCHAR(20), 
#  lname VARCHAR(30), 
#  gender CHAR(1), 
#  joining DATE,
#  birth_date DATE);"""
# # 
# cursor.execute(sql_command) 

sql_command = """INSERT INTO employee_new123 (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "Ann", "Taylor", "F", "1986-10-26");"""
cursor.execute(sql_command)
 
 
sql_command = """INSERT INTO employee_new123 (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "Bruce", "Lee", "M", "1990-08-18");"""
cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()
print("table and data is inserted..")

connection.close()