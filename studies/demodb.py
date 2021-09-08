from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user="root",
    password = "Mostwanted1996*",
    database="demodb"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)",("talha",25))

# db.commit()

# mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M','F','O) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)",('Talha',datetime.now(), "M"))

# db.commit()

# mycursor.execute("SELECT id,name FROM Person WHERE gender = 'M' ORDER BY id DESC")
# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
# mycursor.execute("ALTER TABLE Test DROP food")
# mycursor.execute("ALTER TABLE Test CHANGE first_name VARCHAR(2)")

for x in mycursor:
    print(x)
