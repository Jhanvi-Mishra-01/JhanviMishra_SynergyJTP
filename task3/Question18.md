QUESTION
Given x = np.arange(1, 25).reshape(2, 12), split it into 3 equal parts. Split it after the 3rd and 4th columns. Then split np.arange(1, 7) into 4 parts with np.array_split.

CODE
import numpy as np
x = np.arange(1, 25).reshape(2, 12)
sp1=np.hsplit(x,2)
y=np.arange(1,7)
sp2=np.array_split(y,4)
print(sp1)
print("\n")
print(sp2)

OUTPUT
[array([[ 1,  2,  3,  4,  5,  6],
       [13, 14, 15, 16, 17, 18]]), array([[ 7,  8,  9, 10, 11, 12],
       [19, 20, 21, 22, 23, 24]])]


[array([1, 2]), array([3, 4]), array([5]), array([6])]
