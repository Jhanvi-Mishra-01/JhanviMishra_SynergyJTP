QUESTION
Create the numbers 0 to 9 as int8 and as int64. Print the nbytes of each.

CODE
import numpy as np
for i in range(0,10):
    int8=np.int8(i)
    int64=np.int64(i)
    print("int8: for", i, "is", int8.nbytes)
    print("int64: for",i, "is", int64.nbytes)
    print("\n")

OUTPUT
int8: for 0 is 1
int64: for 0 is 8


int8: for 1 is 1
int64: for 1 is 8


int8: for 2 is 1
int64: for 2 is 8


int8: for 3 is 1
int64: for 3 is 8


int8: for 4 is 1
int64: for 4 is 8


int8: for 5 is 1
int64: for 5 is 8


int8: for 6 is 1
int64: for 6 is 8


int8: for 7 is 1
int64: for 7 is 8


int8: for 8 is 1
int64: for 8 is 8


int8: for 9 is 1
int64: for 9 is 8
