# import time 
# import threading

# start = time. perf_counter()

# def do_something(seconds):
#     print(f'sleeping {seconds} second..')
#     time.sleep(seconds)
#     print('Done sleeping..')

# # t1 = threading.Thread(target=do_something)
# # t2 = threading.Thread(target=do_something)

# threads = []

# for _ in range(10): ## _ is a throw away variable
#     t = threading.Thread(target=do_something, args=[2])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# # t1.start()  #thread run separately then the script code can finish excuting when the treads are asleep
# # t2.start()

# # t1.join() #join so that the script donesnt finish while the threads are sleeping
# # t2.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start,2)} seconds(s)')
############################################################### NEW WAY ###################################

import concurrent.futures
import time

def do_something(seconds):
    print(f'sleeping {seconds} second..')
    time.sleep(seconds)
    print('Done sleeping..')

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1,2,3,4,5]
    result = [executor.submit(do_something,sec) for sec in secs]

    for f in concurrent.futures.as_completed(result):
        print(f.result())

