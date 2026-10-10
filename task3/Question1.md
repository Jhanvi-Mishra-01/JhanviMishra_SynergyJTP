QUESTION
Create an array from [3, 6, 9, 12, 15]. Print its shape, ndim, size and dtype.

CODE
import numpy as np
ar1=np.array([10,20,30,40,50])
print(ar1)
dim=ar1.dtype
print(dim)
print(ar1.shape)
print(ar1.size)
print(ar1.ndim)
ar2=np.ones((3,3), dtype=int)
print(ar2)

OUTPUT
[10 20 30 40 50]
int64
(5,)
5
1
[[1 1 1]
 [1 1 1]
 [1 1 1]]