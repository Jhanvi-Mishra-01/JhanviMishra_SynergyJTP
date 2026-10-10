QUESTION
Given a = np.array([11,11,12,13,14,15,16,17,12,13,11,14,18,19,20]), print the unique values, how many times each occurs, and the first index of each. Expected counts: [3 2 2 2 1 1 1 1 1 1].

CODE
import numpy as np
a = np.array([11,11,12,13,14,15,16,17,12,13,11,14,18,19,20])
unique_val, index, count=np.unique(a, return_index=True, return_counts=True)
print("Unique values:", unique_val)
print("Counts (how many times each occurs):", count)
print("First index of each:", index)

OUTPUT
Unique values: [11 12 13 14 15 16 17 18 19 20]
Counts (how many times each occurs): [3 2 2 2 1 1 1 1 1 1]
First index of each: [ 0  2  3  4  5  6  7 12 13 14]
