import time,multiprocessing

def w(sleeptime)
    time.sleep(sleeptime)
    print(multiprocessing.current_process().name," finished")
    
if __name__=='__main__':
    t=multiprocessing.Process(target=w,args=(10,))
    t.start()
    t.join()