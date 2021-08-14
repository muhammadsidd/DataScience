import concurrent.futures
import threading
import time
import numpy as np
import requests

start = time. perf_counter()
pair_list=[]

def do_something(seconds):
    print(f'sleeping {seconds} second..')
    time.sleep(seconds)
    return f'Done sleeping..{seconds}'

def comparator(a,b):
    global pair_list
    time.sleep(0.5)
    if a + b == 12:
        t = (a,b)
        print(threading.current_thread())
        pair_list.append(t)

nums = [3,9,2,10,6,5,7,4,1,11]
treds = []

for i in range(len(nums)-1):
    thread = threading.Thread(target=comparator,args=(nums[i],nums[i+1]))
    treds.append(thread)

for t in treds:
    t.start()

for t in treds:
    t.join()
    


finish = time.perf_counter()
print(pair_list)
print(f'Finished in {round(finish-start,2)} seconds(s)')


### return job that was started first #####
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results2 = executor.map(do_something,secs)

    for resulted in results2:
        print(resulted)
    
##### return what completed first #######
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


