from threading import Thread
import threading
from pandas.core.frame import DataFrame
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import concurrent.futures
import time
import numpy as np
import requests
import sys
import csv
engine = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="0000",
    host="database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com",
    port='5432'
)
# df = pd.read_csv("developerdata.csv")
# df = pd.read_sql_query('SELECT * FR')
# df.to_sql('Developer',psengine)
# query = 'SELECT "Respondent" FROM public."Developer" WHERE "trnx_id" = \'120\' '


# psengine =  create_engine('postgresql://postgres:0000@database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com:5432/postgres')
# def extraction(query):
#     return pd.read_sql(query,psengine)

#     for resulted in results2:
#         dflist.append(resulted)

# df = pd.concat(dflist,sort=False)

# print(df.head())

# t_path_n_file = "C:\SummitWorks_training\DataScience\studies\users.csv"
# cur.execute(query)
# df = pd.read_csv('user.csv', )
# print(df.head())
# table = 'public."Developer"'
# query = 'SELECT COUNT(*) FROM ' + table+';'
# cur = engine.cursor()
# cur.execute(query)
# l1=[]
# for c in cur:   
#     l1.append(c)

# print(-(-l1[0][0] // 2),type(l1[0][0]))
class DBConnection:
    def __init__(self, **kwargs):
        self.database = kwargs.get('database', '')
        self.user = kwargs.get('user', '')
        self.password = kwargs.get('password', '')
        self.host = kwargs.get('host', '')
        self.port = kwargs.get('port', '')

    def conn(self):
        engine = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)

        return engine
    def cur(self):
        return self.conn().cursor()


class db:
    def __init__(self):
        self.db = DBConnection(database="postgres", user="postgres", password="0000",
                               host="database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com", port='5432')
        self.con = self.db.conn()
        self.cursor = self.db.cur()
        self.psengine =  create_engine('postgresql://postgres:0000@database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com:5432/postgres')

    def insertintotable(self, df, target_table_name):
        
        df.to_sql(target_table_name, self.psengine, if_exists = 'append')

    def readfromtable(self, source_table_name):
        # query = 'SELECT * FROM public."Developer"'
        query = 'SELECT * FROM ' + source_table_name
        SQL_for_file_output = "copy ({0}) to stdout with csv header".format(
            query)
        with open('temp.csv', 'w', encoding="utf-8") as f_output:
            self.cursor.copy_expert(SQL_for_file_output, f_output)
    
    def get_table_columns(self):

        with open('temp.csv', newline='',encoding='utf-8') as f:
            reader = csv.reader(f)
            return next(reader)
    
    def get_chunksize(self, source_table_name,numofthreads):
        query = 'SELECT COUNT(*) FROM ' + source_table_name
        self.cursor.execute(query)
        l1 = []
        for r in self.cursor:
            l1.append(r)

        return l1[0][0] // numofthreads
        

df = pd.DataFrame
workspace = db()
table_n = 'public."Developer"'
threads = 8
target_table = 'public."Developertemp"'
workspace.readfromtable(table_n)
cols  = workspace.get_table_columns()
chunk_size = workspace.get_chunksize(table_n,8)

print(cols)
print(chunk_size)

threads=[]

for chunk in pd.read_csv('temp.csv',chunksize=chunk_size):

    time.sleep(2)

    thread = threading.Thread(target=workspace.insertintotable,args=(chunk,target_table))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()