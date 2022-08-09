"""You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]"""


mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]
k = 3


Count1Map = {}
# making a map of the count of 1s in each row
# here we are using a dictionary to store the count of 1s in each row
# corresponding to the row number

for i in range(len(mat)):
    idx, count = i, mat[i].count(1)
    Count1Map[idx] = count

# Method 1: to get the k weakest rows
vals = sorted(Count1Map.values())
ans = []
for i in range(len(vals)):
    for key, v in Count1Map.items():
        if v == vals[i]:
            if key not in ans:
                ans.append(key)
print(ans)
print(ans[:k])

# Method 2: to get the k weakest rows
from heapq import *

ans = nsmallest(k, Count1Map.items(), key=lambda x: x[1])
final_ans = []
for i in ans:
    final_ans.append(i[0])
print(final_ans)
