import time
import numpy as np
from multiprocessing import Pool, Array, Process

def map_function(subindices):
    for i in subindices:
        B[i] = A[i]
if __name__=='__main__':
    print 'multiprocess version of list (array) copy'
    K = 2*10**3
    proc_num = 2
    attemps = 5
    times = []
    chunks = [range(K*K*i/proc_num,K*K*(i+1)/proc_num ) for i in range(proc_num)]
    indices = range(K*K)
    for _ in xrange(attemps):
        A = np.random.randn(K *K).tolist()
        
        B = Array('f', K*K, lock=False)
        try: 
            pool = Pool(proc_num)
            
            time_start = time.time()
            pool.map(map_function, chunks)
            times.append(time.time() - time_start)
        finally:
            pool.close()
        
        
    print np.mean(times), np.std(times)

