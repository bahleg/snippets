# Simple benchmark for python list copy
The main purpose of this benchmark is to understand whether this simple operation depends on cache using python native structures and common libraries.
## Compared methods:
    1. Naive list copy 
    2. Naive list copy with random index order 
    3. Memoryview copy
    4. Memoryview copy with random index order
    5. Numpy array copy (by indices)
    6. Numpy array copy with random index order
    7. Copy with multiprocessing
    8. Copy with ThreadPool
    9. Copy using cython
    10. Copy using cython with random index order
    11. Copy using cython with prange directive (multithreading without GIL)
    
## Results
Experiments were conducted on laptop with 2 cores, list size is 4*10ˆ6.

|Method                     |Result (sec)|
|---------------------------|------------|
|Naive                      |        0.46|
|Naive with random order    |        1.78|
|Memoryview                 |        1.66|
|MV with random order       |        1.89|
|Numpy                      |        0.42|
|Numpy with random order    |        1.26|
|Multiprocessing            |        0.52|
|ThreadPool                 | (wow!) 0.27|
|Cython                     |        0.04|
|Cython with random order   |        0.78|
|Cython prange              |        0.01|