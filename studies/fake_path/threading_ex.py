import threading
import multiprocessing

def worker(num):
    """ Worker procedure
    """
    print('Worker:', str(num))

jobs = [] # list of jobs
jobs_num = 5 # number of workers
for i in range(jobs_num):
    # Declare a new process and pass arguments to it
    p1 = multiprocessing.Process(target=worker)
    jobs.append(p1)
    # Declare a new process and pass arguments to it
    p2 = multiprocessing.Process(target=worker)
    jobs.append(p2)
    p1.start() # starting workers
    p2.start() # starting workers

for j in jobs:
    j.join()
