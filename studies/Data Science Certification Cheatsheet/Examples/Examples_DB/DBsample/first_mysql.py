import pymysql
# pip install pymysql

# Open database connection
dbconn = pymysql.connect(host="localhost",
                         user="root",
                         password="root",
                         database="python_mysql")

print("database connected")

# prepare a cursor object using cursor() method
with dbconn: #
    with dbconn.cursor() as cursor:
        # Drop table if it already exist using execute() method.
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        # Create table as per requirement
        sql = """CREATE TABLE EMPLOYEE (
                    ID int primary key AUTO_INCREMENT,
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,  
                 GENDER CHAR(1),
                 INCOME FLOAT )"""
        cursor.execute(sql)  # non select
    # connection is not autocommit by default. So you must commit to save your changes.
    dbconn.commit()

# disconnect from server
# dbconn.close()
