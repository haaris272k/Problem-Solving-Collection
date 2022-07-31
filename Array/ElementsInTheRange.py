"""Given an array arr[] containing positive elements.
A and B are two numbers defining a range.
The task is to check if the array contains all elements in the given range.

Example 1:

Input: N = 7, A = 2, B = 5
arr[] =  {1, 4, 5, 2, 7, 8, 3}
Output: Yes
Explanation: It has elements between 
range 2-5 i.e 2,3,4,5"""

# There are many ways to solve this problem.

# M-1:
a, b = 2, 5
arr = [1, 4, 5, 2, 7, 8, 3]

rangeArr = [i for i in range(a, b + 1)]

for i in rangeArr:
    if i not in arr:
        print(False)
print(True)

# M-2:
a, b = 2, 5
arr = [1, 4, 5, 2, 7, 8, 3]

rangeArr = [i for i in range(a, b + 1) if i in arr]
length1 = b - a + 1
length2 = len(rangeArr)

if length1 == length2:
    print(True)
else:
    print(False)

# M-3: using dictionary
from collections import Counter

a, b = 2, 5
arr = [1, 4, 5, 2, 7, 8, 3]

rangeArr = [i for i in range(a, b + 1)]
dicc = Counter(rangeArr)

for k, v in dicc.items():
    if k not in arr:
        print(False)
print(True)
