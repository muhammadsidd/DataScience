import pymysql

conn = pymysql.Connect(host='localhost',user='root',password='root',database='python_mysql')

c = conn.cursor()

# c.execute("""drop table if exists employee""")
# conn.commit()

# c.execute("""create table towns1 (
#         tid        int        primary key not NULL ,
#         name        text,
#         postcode        text)""")
# 
# c.execute("""create table hotels1 (
#         hid        int        primary key not NULL ,
#         tid        int,
#         name        text,
#         address        text,
#         rooms        int,
#         rate        float)""")

c.execute("""insert into towns1 values (1, "Melksham", "SN12")""")
c.execute("""insert into towns1 values (2, "Cambridge", "CB1")""")
c.execute("""insert into towns1 values (3, "Foxkilo", "CB22")""")

c.execute("""insert into hotels1 values (1, 2, "Hamilkilo Hotel", "Chesterton Road", 15, 40.)""")
c.execute("""insert into hotels1 values (2, 2, "Arun Dell", "Chesterton Road", 60, 70.)""")
c.execute("""insert into hotels1 values (3, 2, "Crown Plaza", "Downing Street", 100, 105.)""")
c.execute("""insert into hotels1 values (4, 1, "Well House Manor", "Spa Road", 5, 80.)""")
c.execute("""insert into hotels1 values (5, 1, "Beechfield House", "The Main Road", 26, 110.)""")

conn.commit()

c.execute ("""select * from towns1 left join hotels1 on towns1.tid = hotels1.tid""")

for row in c:
        print (row)

c.close()