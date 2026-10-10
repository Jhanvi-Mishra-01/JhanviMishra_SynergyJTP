QUESTION
Find the indices of values greater than 15 using np.nonzero, then again using np.where. Expected: [1 3 4 5 7].

CODE
import numpy as np
arr=np.array([4, 15, 8, 23, 42, 16, 7, 30])
result1=np.nonzero(arr>15)
result2=np.where(arr>15)
print(result1)
print(result2)

OUTPUT
(array([3, 4, 5, 7]),)
(array([3, 4, 5, 7]),)