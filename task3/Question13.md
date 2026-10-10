QUESTION
Given x = np.array([[1,2,3],[4,5,6]]), create f = x.flatten() and r = x.ravel(). Set f[0] = 100 and r[1] = 200, then print x.

CODE
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print(x)
f=x.flatten()
r=x.ravel()
f[0]=100
r[1]=200
print(x)

OUTPUT
[[1 2 3]
 [4 5 6]]
[[  1 200   3]
 [  4   5   6]]