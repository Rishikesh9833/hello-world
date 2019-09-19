import time,multiprocessing
import requests,concurrent.futures

def download(url):
    print(multiprocessing.current_process().name,url)
    con = requests.get(url)
    return [url,len(con.text)]
    
if __name__=='__main__':
    urls =['http://www.google.co.in' for _ in range(10)]
    st = time.time()
    print('seq')
    r = download(urls[0])
    one = time.time() - st
    print(r, " took",one," secs")
    print("now parallel")
    ex = concurrent.futures.ProcessPoolExecutor(max_workers=10)
    st = time.time()
    rs= ex.map(download,urls)
    print(list(rs)," took",time.time()-st, " supported to take",one*10," secs in you do seq")
    ex.shutdown()