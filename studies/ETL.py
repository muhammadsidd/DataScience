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
import configparser
import logging


engine = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="",
    host="database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com",
    port='5432'
)

class DBConnection:
    def __init__(self,logger  = None, **kwargs):
        if logger is None:
            self.logger = logger
        self.database = kwargs.get('database', '')
        self.user = kwargs.get('user', '')
        self.password = kwargs.get('password', '')
        self.host = kwargs.get('host', '')
        self.port = kwargs.get('port', '')

    def conn(self):
        try:
            engine = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port)
        except Exception as e:
            conn =  None
            self.logger.error("get_connection: " +  str(e))
            return -1

        return engine

    def cur(self):
        return self.conn().cursor()
    def get_tbl_cols(self,query,values):
        cur = None
        status = -1
        resultset = []
        try:
            cur = self.getcursor()
            if True:
                cur.arraysize = 1
                cur.execute(query,values)
                col_names = []
                for i in range(0,len(cur.description)):
                    col_names.append(cur.description[i][0])
                    resultset = col_names
                    status = 0
        except psycopg2.DatabaseError as e:
            self.logger.error("check_connection" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            self.logger.error("delete_data" +  str(e))
            resultset = e
        
        return status, resultset
    
    def get_tbl_clm_dtypes(self,query,values):
        cur = None
        status = -1
        resultset = []
        try:
            cur = self.getcursor()
            if True:
                cur.arraysize = 1
                cur.execute(query,values)
                col_name_dtypes = []
                for row in [row[1] for row in cur.description]:
                    row = str(row)
                    row = row.replace('class','')
                    row = row.replace('psycopg2','')
                    row = row.replace('DbType DB_TYPE_','')
                    row = row.replace('<','')
                    row = row.replace('>','')
                    row = row.replace("'",'')
                    col_name_dtypes.append(row)
                    resultset = col_name_dtypes
                    status = 0
        except psycopg2.DatabaseError as e:
            self.logger.error("clm_tbl_dtp" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            self.logger.error("clm_tbl_dataype" +  str(e))
            resultset = e
        
        return status, resultset


class db:
    def __init__(self):
        try:
            self.db = DBConnection(database="postgres", user="postgres", password="Mostwanted1996*",
                                host="database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com", port='5432')
            self.con = self.db.conn()
            self.cursor = self.db.cur()
            self.psengine =  create_engine('postgresql://postgres:0000@database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com:5432/postgres')

        except Exception as e:
            conn =  None
            self.logger.error("get_connection: " +  str(e))
            return -1

    def insertintotable(self, df, target_table_name):
        try:
            df.to_sql(target_table_name, self.psengine, if_exists = 'append')
        except Exception as e:
            conn =  None
            self.logger.error("inset_into_tables " +  str(e))
            return -1

    def readfromtable(self, source_table_name):
        # query = 'SELECT * FROM public."Developer"'
        query = 'SELECT * FROM ' + source_table_name
        SQL_for_file_output = "copy ({0}) to stdout with csv header".format(
            query)
        try:
            with open('temp.csv', 'w', encoding="utf-8") as f_output:
                self.cursor.copy_expert(SQL_for_file_output, f_output)
        except Exception as e:
            conn =  None
            self.logger.error("get_connection: " +  str(e))
            return -1
    
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

    def get_respondant(self):
        query = 'SELECT "Respondent" FROM public."Developer" WHERE "index" = \'120\' '
        try:
            self.cursor.execute(query)
        except Exception as e:
            conn =  None
            self.logger.error("get_connection: " +  str(e))
            return -1

        for r in self.cursor:
            print(r)
    

def do_start():

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

    workspace.get_respondant()
