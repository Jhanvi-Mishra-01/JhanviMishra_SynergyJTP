QUESTION
Use a = np.arange(1, 36).reshape(5, 7). Print the 3rd row, the 4th column, the last row and the last column.

CODE
import numpy as np
a=np.arange(1,36).reshape(5,7)
print(a[2,:])
print(a[:,3])
print(a[-1,:])
print(a[:,-1])

OUTPUT
[15 16 17 18 19 20 21]
[ 4 11 18 25 32]
[29 30 31 32 33 34 35]
[ 7 14 21 28 35]