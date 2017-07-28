import time
import numpy as np
print 'matrix copy with random index order'
K = 2*10**3
attemps = 5
times = []
indices = range(K*K)

for _ in xrange(attemps):
    A = np.random.randn(K *K).tolist()
    
    B = [0 for _ in xrange(K*K)]
    np.random.shuffle(indices)
    time_start = time.time()
    for i in indices:
        B[i] = A[i]
    times.append(time.time() - time_start)
print np.mean(times), np.std(times)


