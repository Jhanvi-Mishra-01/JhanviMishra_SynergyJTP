QUESTION
With rng = np.random.default_rng(), create a 3x3 array of random floats and a 2x5 array of random integers from 0 to 9. Then use np.random.randint to create a 4x4 array of integers from 1 to 100.

CODE
import numpy as np
rng=np.random.default_rng()
floats=rng.random((3,3))
random_int=rng.integers(0,10, (2,5))
randint=np.random.randint(1,101, (4,4))
print(floats)
print("\n")
print(random_int)
print("\n")
print(randint)

OUTPUT
[[0.62980916 0.39921649 0.42920957]
 [0.49121796 0.32930757 0.8386026 ]
 [0.90135406 0.27828077 0.94510584]]


[[0 9 0 9 8]
 [9 1 0 4 8]]


[[26 22 19 29]
 [94 50 73 67]
 [ 9 53 25 77]
 [86 78 97  9]]