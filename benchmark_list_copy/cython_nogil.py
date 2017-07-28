import time
import numpy as np
import os 

import cython_funcs 
print 'list (array) copy with multiple threads and cython nogil'
K = 2*10**3
attemps = 5
block_size = 200
threads = 2 
times = []
indices = range(K*K)

for _ in xrange(attemps):
    A = np.random.randn(K * K)
    A = np.array(A)
    B = np.zeros(K*K)
    np.random.shuffle(indices)
    time_start = time.time()
    
    B = cython_funcs.make_copy_nogil(A, B,  threads)
    times.append(time.time() - time_start)
print np.mean(times), np.std(times)

