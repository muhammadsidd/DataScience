import concurrent.futures
import time
import numpy as np
import requests

start = time. perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} second..')
    time.sleep(seconds)
    return f'Done sleeping..{seconds}'


##### return what completed first #######
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

### return job that was started first #####

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results2 = executor.map(do_something,secs)

    for resulted in results2:
        print(resulted)

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds(s)')

print(int(False))
print("123".replace("12", "ab"))
print({'a','b'} &{'a'})
print(len(("disco",10,1.2, "hard rock",10)))

for i,x in enumerate(['A','B','C']):
    print(i,2*x)

a=1

def do(x):
    return(x+a)

print(do(1))

X=np.array([[1,0,1],[2,2,2]]) 
out=X[0,1:3]
print(out)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y)
print(Z)

######## with while loop ######
File1 = open("Example1.txt","r")
file_stuff=File1.readline (4)
print(file_stuff)
# while file_stuff:
#     print(file_stuff)
#     file_stuff = File1.readline()
# File1.close()

###### for loop #############

with open("Example1.txt","r") as File2:
    for line in File2.readlines():
        print(line)

url = 'https://www.ibm.com'
# r = requests.get(url)
# print(r.status_code, r.request.headers, r.headers) #r.headers = response headers 
payload = {"name": 'Joseph', "ID":223}
r = requests.get(url, params=payload)
print(r.url)

print(2/2)