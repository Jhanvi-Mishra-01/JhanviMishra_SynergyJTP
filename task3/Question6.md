QUESTION
Use the same array from Question 5. Print every second element of the first row. Print the 2x3 block from rows 1 to 2 and columns 2 to 4.

CODE
import numpy as np
a=np.arange(1,36).reshape(5,7)
print(a[0,::2])
print(a[1:3,2:5])

OUTPUT
[1 3 5 7]
[[10 11 12]
 [17 18 19]]