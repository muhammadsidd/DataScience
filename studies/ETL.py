import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import concurrent.futures
import time
import numpy as np
import requests

# engine = psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="Mostwanted1996*",
#     host="database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com",
#     port='5432'
# )
# df = pd.read_csv("developerdata.csv")
# df = pd.read_sql_query('SELECT * FR')
# df.to_sql('Developer',psengine)
# query = 'SELECT "Respondent" FROM public."Developer" WHERE "trnx_id" = \'120\' '


psengine =  create_engine('postgresql://postgres:Mostwanted1996*@database-2.c96jpumhdub0.us-east-2.rds.amazonaws.com:5432/postgres')
def extraction(query):
    return pd.read_sql(query,psengine)

with concurrent.futures.ThreadPoolExecutor() as executor:
    queries = [' SELECT * FROM public."Developer" where "Respondent" % 2 = 0',' SELECT * FROM public."Developer" where "Respondent" % 2 != 0']
    results2 = executor.map(extraction,queries)
    dflist = []
    
    for resulted in results2:
        dflist.append(resulted)

df = pd.concat(dflist,sort=False)

print(df.head())


