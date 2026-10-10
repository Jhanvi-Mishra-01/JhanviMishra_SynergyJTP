QUESTION
Given a = np.array([1, 2, 3, 4, 5, 6]), make a row vector (1, 6) and a column vector (6, 1). Do it once with np.newaxis and once with np.expand_dims.

CODE
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
col1=a[:,np.newaxis]
row1=a[np.newaxis,:]
row2=np.expand_dims(a, axis=0)
col2=np.expand_dims(a, axis=1)
print(row1)
print(col1)
print("\n")
print(row2)
print(col2)

OUTPUT
[[1 2 3 4 5 6]]
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]


[[1 2 3 4 5 6]]
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]