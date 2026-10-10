QUESTION
Create a = np.arange(1, 9) and b = a[2:6]. Set b[0] = 99 and print a. Repeat with b = a[2:6].copy() and print a again.

CODE
import numpy as np
a=np.arange(1,9)
b=a[2:6]
b[0]=99
print(a)
b=a[2:6].copy()
print(a)

OUTPUT
[ 1  2 99  4  5  6  7  8]
[ 1  2 99  4  5  6  7  8]