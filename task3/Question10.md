QUESTION
Given marks = np.array([[45,80,67],[90,55,72],[38,60,85]]), print the marks that are 60 or above. Then count how many students scored 40 or more in each subject (column). Expected: [2 3 3].

CODE
import numpy as np
marks = np.array([[45,80,67],[90,55,72],[38,60,85]])
above_60=marks[marks>=60]
print(above_60)
above_40=(marks>=40).sum(axis=0)
print(above_40)

OUTPUT
[80 67 90 72 60 85]
[2 3 3]