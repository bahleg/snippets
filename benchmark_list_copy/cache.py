import time
import numpy as np
print 'simple list (array) copy'
K = 2*10**3
attemps = 5
times = []
indices = range(K*K)
for _ in xrange(attemps):
    A = np.random.randn(K *K).tolist()
    
    B =  [0]*(K*K)
    time_start = time.time()
    for i in indices:
        B[i] = A[i]
    assert B==A
    times.append(time.time() - time_start)
print np.mean(times), np.std(times)

