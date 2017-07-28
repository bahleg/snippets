import time
import numpy as np
print 'memroy-view version of list (array) copy'
K = 2*10**3
indices = range(K*K)
attemps = 5
times = []

for _ in xrange(attemps):
    A = memoryview(bytearray(np.random.randn(K * K).astype(np.float64).tostring()))
    B = memoryview(bytearray(np.zeros((K * K)).astype(np.float64).tostring()))

    time_start = time.time()
    
    print 'transposing'
    for i in indices:
        start_byte = i*4
        B[start_byte:start_byte+4] = A[start_byte:start_byte+4]
    times.append(time.time() - time_start)
print np.mean(times), np.std(times)
