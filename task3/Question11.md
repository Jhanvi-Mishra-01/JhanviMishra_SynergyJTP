QUESTION
Given s = np.array([2, 5, 8, 11, 14]), use np.searchsorted to find where 9 would be inserted. Then do it for [1, 12, 5] in one call. Expected: 3, then [0 4 1].

CODE
import numpy as np
s = np.array([2, 5, 8, 11, 14])
add=np.searchsorted(s, 9)
print(add)
add2=np.searchsorted(s, [1,12,5])
print(add2)

OUTPUT
3
[0 4 1]