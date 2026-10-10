QUESTION
Create a 3x2 array of zeros, a 2x4 array of ones with dtype=int, and a 2x3 array filled with 7 using np.full.

CODE
import numpy as np
zero=np.zeros((3,2))
ones=np.ones((2,4), dtype=int)
seven=np.full((2,3), 7)
print(zero)
print(ones)
print(seven)

OUTPUT
[[0. 0.]
 [0. 0.]
 [0. 0.]]
[[1 1 1 1]
 [1 1 1 1]]
[[7 7 7]
 [7 7 7]]