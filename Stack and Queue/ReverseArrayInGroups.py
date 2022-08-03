"""Given an array arr[] of positive integers of size N. 
Reverse every sub-array group of size K.

 

Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5."""


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(arr)

# Method 1
# Slicing
print(arr[:k][::-1] + arr[k:])

# Method 2
# Using stack
TempStack = []
for i in range(k):
    ele = arr.pop(0)
    TempStack.append(ele)
TempStack.reverse()
TempStack.extend(arr)
arr = TempStack
print(arr)
