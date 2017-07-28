import time
import numpy as np
from multiprocessing.pool import ThreadPool

def map_function(subindices):
    for i in subindices:
        B[i] = A[i]
if __name__=='__main__':
    print 'list (array) copy using thread-pool'
    K = 2*10**3
    proc_num = 1
    attemps = 5
    times = []
    chunks = [range(K*K*i/proc_num,K*K*(i+1)/proc_num ) for i in range(proc_num)]
    indices = range(K*K)
    for _ in xrange(attemps):
        A = np.random.randn(K *K).tolist()
        
        B =  [0]*(K*K)
        try: 
            pool = ThreadPool(proc_num)
            
            time_start = time.time()
            pool.map(map_function, chunks)
            #map_function(chunks[0])
            times.append(time.time() - time_start)
            assert B==A
        finally:
            pool.close()
        
        
    print np.mean(times), np.std(times)

