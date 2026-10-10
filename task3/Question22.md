QUESTION
Write code that tries each of these additions and prints the result shape or the error message: (4,3)+(3,), (4,3)+(4,), (4,3)+(4,1), (2,3,4)+(3,1). Use np.ones for the arrays.

CODE
import numpy as np
a1=np.ones((4,3))
a2=np.ones((1,3))
a3=np.ones((4,))
a4=np.ones((4,1))
a5=np.ones((2,3,4))
a6=np.ones((3,1))

try:
    r1=a1+a2
    print(r1)
    print("\n")
except:
    print(f"Broadcasting not possible for {(4,3)} and {(3,)}")
try:
    r2=a1+a3
    print(r2)
    print("\n")
except:
    print(f"Broadcasting not possible for {(4,3)} and {(4,)}")
try:
    r3=a1+a4
    print(r3)
    print("\n")
except:
    print(f"Broadcasting not possible for {(4,3)} and {(4,1)}")
try:
    r4=a5+a6
    print(r4)
    print("\n")
except:
    print(f"Broadcasting not possible for {(2,3,4)} and {(3,1)}")



OUTPUT
[[2. 2. 2.]
 [2. 2. 2.]
 [2. 2. 2.]
 [2. 2. 2.]]


Broadcasting not possible for (4, 3) and (4,)
[[2. 2. 2.]
 [2. 2. 2.]
 [2. 2. 2.]
 [2. 2. 2.]]


[[[2. 2. 2. 2.]
  [2. 2. 2. 2.]
  [2. 2. 2. 2.]]

 [[2. 2. 2. 2.]
  [2. 2. 2. 2.]
  [2. 2. 2. 2.]]]
