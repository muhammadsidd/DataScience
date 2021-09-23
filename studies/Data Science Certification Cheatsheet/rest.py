from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()
def g(d, l):
    d[4] = '1'
    d['3'] = 2
    d[0.15] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p1=Process(target=g,args=(d,l))
        p.start()
        p1.start()
        p.join()
        p1.join()
        print(d)
        print(l)