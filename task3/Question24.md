QUESTION
Given A = [[1,2],[3,4]] and B = [[5,6],[7,8]], print the element-wise product, the matrix product with np.matmul ([[19 22] [43 50]]), and the determinant of A with np.linalg.det (-2.0).

CODE
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
ele_prod=a*b
print(ele_prod)
print("\n")
mat_prod=np.matmul(a,b)
print(mat_prod)
print("\n")
det=np.linalg.det(a)
print(det)

OUTPUT
[[ 5 12]
 [21 32]]


[[19 22]
 [43 50]]


-2.0000000000000004