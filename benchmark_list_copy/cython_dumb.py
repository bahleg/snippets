import time
import numpy as np
import os 

import cython_funcs
print 'cython version of list (array) copy with random index order'
K = 2*10**3
attemps = 5
block_size = 200
times = []
indices = range(K*K)

for _ in xrange(attemps):
    A = np.random.randn(K * K)
    A = np.array(A)
    B = np.zeros(K*K)
    np.random.shuffle(indices)
    time_start = time.time()
    
    B = cython_funcs.make_copy(A, B,  indices)
    times.append(time.time() - time_start)
print np.mean(times), np.std(times)

