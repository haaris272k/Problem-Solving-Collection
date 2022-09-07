"""Given an array arr[] of size N containing equal number of odd and even numbers. 
Arrange the numbers in such a way that all the even numbers get the even index and
odd numbers get the odd index.
Note: There are multiple possible solutions, 
Print any one of them. Also, 0-based indexing is considered.

 

Example 1:

Input:
N = 6
arr[] = {3, 6, 12, 1, 5, 8}
Output:
1
Explanation:
6 3 12 1 8 5 is a possible solution.
The output will always be 1 if your
rearrangement is correct."""


arr = [3, 6, 12, 1, 5, 8]

# TC: O(n)
# SC: O(n)

n = len(arr)
hashtable = {"even": [], "odd": []}
for i in arr:
    if i % 2 == 0:
        hashtable["even"].append(i)
    else:
        hashtable["odd"].append(i)
arr.clear()

for i in range(n):
    if i % 2 == 0:
        arr.append(hashtable["even"].pop())
    else:
        arr.append(hashtable["odd"].pop())

print(arr)
