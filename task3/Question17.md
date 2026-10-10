QUESTION
Given a1 = [[1,1],[2,2]] and a2 = [[3,3],[4,4]], produce the vstack result, the hstack result, and np.concatenate along axis=1.

CODE
import numpy as np
a1 = [[1,1],[2,2]]
a2 = [[3,3],[4,4]]
vstack=np.vstack((a1,a2))
hstack=np.hstack((a1,a2))
con=np.concatenate((a1,a2), axis=1)
print(vstack)
print("\n")
print(hstack)
print("\n")
print(con)

OUTPUT
[[1 1]
 [2 2]
 [3 3]
 [4 4]]


[[1 1 3 3]
 [2 2 4 4]]


[[1 1 3 3]
 [2 2 4 4]]