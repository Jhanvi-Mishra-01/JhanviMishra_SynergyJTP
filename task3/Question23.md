QUESTION
Create a 3x4 array with rng.random. Print its overall sum, mean, min, max, std and prod, then the column sums, the row maxima, and the index of the overall maximum.

CODE
import numpy as np
rng=np.random.default_rng()
arr=rng.random((3,4))
asum=arr.sum()
amean=arr.mean()
amin=arr.min()
amax=arr.max()
astd=arr.std()
aprod=arr.prod()
acol_sum=arr.sum(axis=0)
row_max=arr.max(axis=0)
max_index=arr.argmax()

print(asum)
print(amean)
print(amin)
print(amax)
print(astd)
print(aprod)
print(acol_sum)
print(row_max)
print(max_index)

OUTPUT
4.348834791745353
0.3624028993121127
0.05380416998073856
0.9199584737287445
0.27720274951315826
9.219790329204884e-08
[0.83707211 0.95467096 1.09194453 1.46514719]
[0.49219376 0.40371256 0.91995847 0.90205615]
2
