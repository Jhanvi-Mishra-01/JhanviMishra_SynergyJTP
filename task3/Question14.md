QUESTION
Reshape np.arange(1, 13) into (3, 4), (2, 6), (2, 3, 2) and (4, -1). Print the shape of each.

CODE
import numpy as np
first=np.arange(1,13).reshape(3,4)
sec=np.arange(1,13).reshape(2,6)
third=np.arange(1,13).reshape(2,3,2)
fourth=np.arange(1,13).reshape(4,-1)
print(first)
print("\n")
print(sec)
print("\n")
print(third)
print("\n")
print(fourth)

OUTPUT
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]


[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]


[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]


[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]