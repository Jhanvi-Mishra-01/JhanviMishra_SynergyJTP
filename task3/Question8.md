QUESTION
Use arr = np.array([4, 15, 8, 23, 42, 16, 7, 30]). Print the values greater than 10, the even values, and the values from 10 to 30 inclusive.

CODE
import numpy as np
arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
greater=arr[arr>10]
even=arr[arr%2==0]
inclusive=arr[(arr>=10) & (arr<=30)]
print(greater)
print(even)
print(inclusive)

OUTPUT
[15 23 42 16 30]
[ 4  8 42 16 30]
[15 23 16 30]