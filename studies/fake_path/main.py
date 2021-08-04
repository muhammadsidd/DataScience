import concurrent.futures
import time


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
