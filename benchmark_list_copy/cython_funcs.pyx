import numpy as np
cimport numpy as np
import time 
from cython.parallel import parallel, prange

cpdef make_copy(double[:] A, double[:] B, list indices):
    cdef int i 
    for i in indices:
        B[i] = A[i]
        
cpdef make_copy_nogil(double[:] A, double[:] B, int threads):
    cdef int length = A.shape[0]
    cdef int i 
    with nogil:
        for i in prange(0, length, schedule='static',  chunksize=length/threads, num_threads=threads):
            B[i] = A[i]
            
cpdef double[:, :] dumb_transpose(double[:, :] B):
    time_s = time.time()
    cdef int i
    cdef int j
    cdef double[:,:] A = np.zeros((B.shape[0], B.shape[1]))

    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            A[i,j] = B[j,i]
    print time.time() - time_s
    return A 

cpdef double[:,:] block_transpose(double[:,:] B, int block_size):
        time_s = time.time()
        cdef int i
        cdef int i0
        cdef int j
        cdef int j0
        cdef int K = B.shape[0]
        cdef double[:,:] A = np.zeros((B.shape[0], B.shape[1]))

        for i in  range(0, K, block_size):
            for j in  range(0, K, block_size):

                for i0 in range(i, i+block_size):
                        
                    for j0 in range(j, j+block_size):
                        
                        A[i0, j0] = B[j0, i0]
        print time.time() - time_s 
        return A    
