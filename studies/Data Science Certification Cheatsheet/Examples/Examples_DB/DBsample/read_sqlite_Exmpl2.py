import sqlite3

connection = sqlite3.connect("mytestdb.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM test")

# print("fetchall:")
# result = cursor.fetchall()
# for r in result:
#     print(r)

cursor.execute("SELECT * FROM test")
print("\nfetch one:")
res = cursor.fetchone()
print(res)