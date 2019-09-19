import time,threading
shared=[]

def proc(lck):
    global shared
    print("Before",threading.current_thread().getName())
    with lck:
        time.sleep(2)
        print("Accquired",threading.current_thread().getName())
    time.sleep(2)
    
if __name__=='__main__':
    ids=[]
    #lock = threading.RLock()
    lock = threading.Semaphore(2) # for 2 at time
    for i in range(10):
        t=threading.Thread(target=proc,args=(lock,))
        ids.append(t)
    [t.start() for t in ids]
    [t.join() for t in ids]