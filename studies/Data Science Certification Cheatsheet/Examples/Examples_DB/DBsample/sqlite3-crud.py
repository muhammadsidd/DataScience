import sqlite3


def insert(db, row):
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
    db.commit()


def retrieve(db, t1):
    cursor = db.execute('select * from test where t1 = ?', (t1,)) #rows
    return cursor.fetchone() #(), [(),(),()...]


def update(db, row):
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit()


def delete(db, t1):
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit()


def disp_rows(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))


def main():
    db = sqlite3.connect('mytestdb.db')
    db.row_factory = sqlite3.Row
    print('Create table test')
    # db.execute('drop table if exists test')
    # db.execute('create table test ( t1 text, i1 int )')

    print("**********************1.insert records**********************");
    print("**********************2.delete records**********************");
    print("**********************3.update records**********************");
    print("**********************4.select records**********************");

    option = int(input("enter your option"))
    if option == 1:
        name = input("enter the name")
        value = int(input("enter the value"))
        insert(db, dict(t1=name, i1=value))
        # print('Create rows')
        # insert(db, dict(t1 = 'one', i1 = 1))
        # insert(db, dict(t1 = 'two', i1 = 2))
        # insert(db, dict(t1 = 'three', i1 = 3))
        # insert(db, dict(t1 = 'four', i1 = 4))
        disp_rows(db)
    elif option == 2:
        name = input("Please enter the name to delete from database")
        delete(db, name)
        print("record has been deleted")
    elif option == 3:
        name = input("enter the name name in which the vlaue to upldate")
        value = input("enter the value to update for the above name")
        update(db, dict(t1=name, i1=value))
    elif option == 4:
        disp_rows(db)


if __name__ == "__main__": main()
