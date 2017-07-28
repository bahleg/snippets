import time
import numpy as np
print 'numpy version of matrix copy'
K = 2*10**3
attemps = 5
times = []
indices = range(K*K)
for _ in xrange(attemps):
    A = np.random.randn(K * K)
    B = np.zeros((K*K))
    time_start = time.time()
    B[indices] = A[indices]
    times.append(time.time() - time_start)
print np.mean(times), np.std(times)
