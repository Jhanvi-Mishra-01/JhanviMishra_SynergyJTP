QUESTION
Given a = np.array([1,2,3,4,5]) and b = np.array([4,5,6,7]), compute the union, intersection, difference (a minus b) and symmetric difference. Expected: [1..7], [4 5], [1 2 3], [1 2 3 6 7].

CODE
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7])
union=np.union1d(a,b)
intersection=np.intersect1d(a,b)
difference=np.setdiff1d(a,b)
symm_diff=np.setxor1d(a,b)
print(union)
print(intersection)
print(difference)
print(symm_diff)

OUTPUT
[1 2 3 4 5 6 7]
[4 5]
[1 2 3]
[1 2 3 6 7]