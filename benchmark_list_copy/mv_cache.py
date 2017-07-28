import time
import numpy as np
print 'memory-view version of list(array) copy'
K = 2*10**3
attemps = 5
times = []
indices = range(K*K)
for _ in xrange(attemps):
 
    A = memoryview(bytearray(np.random.randn(K * K).astype(np.float64).tostring()))
    B = memoryview(bytearray(np.zeros((K * K)).astype(np.float64).tostring()))
    time_start = time.time()
    print 'transposing'
    for i in indices:
            B[i:i+4] = A[i:i+4]
    times.append(time.time() - time_start)
print np.mean(times), np.std(times)
