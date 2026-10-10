QUESTION
Given m = np.arange(1, 10).reshape(3, 3), add the row [10, 20, 30] to every row. Then add the column ​[[100], [200], [300]] to every column.

CODE
import numpy as np
m = np.arange(1, 10).reshape(3, 3)
print(m)
row=np.array([10,20,30])
col=np.array([[100],[200],[300]])
print("\n")
m=m+row
print("\n")
m=m+col

OUTPUT
[[1 2 3]
 [4 5 6]
 [7 8 9]]


[[11 22 33]
 [14 25 36]
 [17 28 39]]


[[111 122 133]
 [214 225 236]
 [317 328 339]]