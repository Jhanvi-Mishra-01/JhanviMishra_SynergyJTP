QUESTION
Given a 3x4 array of 1 to 12, print np.flip with no axis, with axis=0 and with axis=1.

CODE
import numpy as np
a=np.arange(1,13).reshape(3,4)
a1=np.flip(a, axis=None)
a2=np.flip(a,axis=0)
a3=np.flip(a,axis=1)
print(a1)
print("\n")
print(a2)
print("\n")
print(a3)

OUTPUT
[[12 11 10  9]
 [ 8  7  6  5]
 [ 4  3  2  1]]


[[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]


[[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]]
