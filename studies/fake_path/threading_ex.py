import threading
import time

lock = threading.Lock()
num_list=[3,9,2,10,6,5,7,4,1,11]
count = 0 
pairval = []


def test():
    global num_list
    global count
    global pairval
    
    while count < len(num_list)-1:

        j = count +1

        while j < len(num_list):

            lock.acquire()

            if num_list[count] + num_list[j] == 12:
                t =(num_list[count],num_list[j])
                pairval.append(t)

            lock.release()
            
            j = j+1
        
        lock.acquire()

        if count<len(num_list):
            count+=1

        lock.release()
        


thread_list=[]
start = time.perf_counter()

thread1 = threading.Thread(target=test)
thread2 = threading.Thread(target=test)
thread3 = threading.Thread(target=test)
thread4 = threading.Thread(target=test)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end = time.perf_counter()

print(pairval)
print(end-start)