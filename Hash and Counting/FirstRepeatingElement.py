"""Given an array arr[] of size n, find the first repeating element.
The element should occurs more than once and the index of its first occurrence should be the smallest.

 

Example 1:

Input:
n = 7
arr[] = {1, 5, 3, 4, 3, 5, 6}
Output: 2
Explanation: 
5 is appearing twice and 
its first appearence is at index 2 
which is less than 3 whose first 
occuring index is 3."""


from collections import OrderedDict

# Using OrderedMap
arr = [1, 5, 3, 4, 3, 5, 6]
n = len(arr)
map = OrderedDict()
for i in range(n):
    if arr[i] in map:
        map[arr[i]] += 1
    else:
        map[arr[i]] = 1

for i in range(n):
    if map[arr[i]] > 1:
        print(i + 1)
        break
else:
    print(-1)
