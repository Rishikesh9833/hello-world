import time,multiprocessing
#shared=[]

def proc(lck,shared):
    #global shared
    print("Before",multiprocessing.current_process().name)
    with lck:
        time.sleep(2)
        print("Accquired",multiprocessing.current_process().name)
        shared.value +=1
    time.sleep(2)
    
if __name__=='__main__':
    ids=[]
    shared=multiprocessing.Value('i',0,lock=False)
    #lock = multiprocessing.RLock()
    lock = multiprocessing.Semaphore(2) # for 2 at time
    for i in range(10):
        t=multiprocessing.Process(target=proc,args=(lock,shared))
        ids.append(t)
    [t.start() for t in ids]
    [t.join() for t in ids]