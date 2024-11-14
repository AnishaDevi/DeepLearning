import numpy as np
import time

a = np.random.rand(10000000)
b = np.random.rand(10000000)

#Vectorized Version
tic = time.time()
c = np.dot(a,b)
toc = time.time()
print(c)
print("Vectorized version time taken:",str(1000*(toc-tic))+"ms\n")

#Non Vectorized Version
c = 0
tic = time.time()
for i in range(10000000):
    c += a[i] * b[i]
toc = time.time()
print(c)
print("Non Vectorized version time taken:",str(1000*(toc-tic))+"ms")
