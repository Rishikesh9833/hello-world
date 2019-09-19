import time,threading

def w(sleeptime):
    time.sleep(sleeptime)
    print(threading.current_thread().getName()," finished")
    
if __name__=='__main__':
    t=threading.Thread(target=w,args=(10,))
    t.start()
    t.join()