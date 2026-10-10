QUESTION
Given arr = np.arange(1, 13).reshape(2, 2, 3), print 6, then the first row of the second block ([7 8 9]), then the last element using negative indices (12).

CODE
import numpy as np
arr = np.arange(1, 13).reshape(2, 2, 3)
print(arr[0,1,2])#print 6
print(arr[1,0,:])
print(arr[-1,-1,-1])

OUTPUT
6
[7 8 9]
12