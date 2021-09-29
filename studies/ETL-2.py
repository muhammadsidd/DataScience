import multiprocessing as mp
import numpy as np
import tqdm
from itertools import repeat
from multiprocessing import Process, Manager
from multiprocessing import Pool
import pandas as pd
import datetime
import time

def process_rows(data):
    d = data[0]
    df = data[1]
    for index,row in df.iterrows():
        ecode = int(row['employee_code'])
        month = int(row['date'].month)
        efficiency = int(row['efficiency'])
        if (ecode,month) in list(d.keys()):
            d[ecode,month] = (efficiency + d[ecode,month]) / 2
        else:
            d[ecode,month] = efficiency

num_processes = mp.cpu_count()

print("Number of cpu : ", num_processes)

employee_df = pd.read_csv('employee.csv',low_memory=False)
data_df = pd.read_csv('data.csv',low_memory=False)

data_df['date']= pd.to_datetime(data_df['date']) 

print(employee_df.head())
print(data_df.head())

name_dict = {}
for index,row in employee_df.iterrows():
    name_dict[row['ecode']] = row['ename']

empcodes= []
empcodes.extend(list(data_df['employee_code'].unique()))

    
print(name_dict)
print(empcodes[:10])

num_partitions = num_processes
manager = Manager()
d = manager.dict()
df_split = np.array_split(data_df, num_partitions)
pool = Pool(num_processes)
shared_arg = repeat(d,num_partitions)
for _ in tqdm.tqdm(pool.map(process_rows, zip(shared_arg,df_split)), total=num_partitions):
    pass
pool.close()
pool.join()

months = []
for i in range(1,13):
    month = datetime.date(1900,i, 1).strftime('%B')
    months.append(month)


################################# PD MULTI PROCESS Different EG ###############################


pool_size = 5

pool = Pool(pool_size)


def add(a,b):
    sum = a+b
    time.sleep(2) #just to show that in reality my function takes times
    print("sum of %d and %d is %d" %(a, b, sum))

data = [[10,10],[9,12],[100,13]]
df = pd.DataFrame(data,columns=['col_1','col_2'])

start_time = time.time()
for ind in df.index:
     pool.apply_async(add, args=(df['col_1'][ind], df['col_2'][ind],))
pool.close()
pool.join()
