"""Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9."""


arr = [2, 3, 4, 7, 11]
k = 5

# TC: O(n^2)
lst = []
for i in range(1, max(arr) + 1 + k):
    if i not in arr:
        lst.append(i)
print(lst[k - 1])

# TC: O(n)
l = list(range(1, len(arr) + k + 1))
l = list(set(l) - set(arr))
l.sort()
print(l[k - 1])
