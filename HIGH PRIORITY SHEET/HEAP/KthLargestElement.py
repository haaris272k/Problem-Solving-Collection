"""Given an array of N positive integers, print k largest elements from the array. 

Example 1:

Input:
N = 5, k = 2
arr[] = {12,5,787,1,23}
Output: 787 23"""

import heapq


li = [1, 23, 12, 9, 30, 2, 50]
k = 3

heap = []
ans = []

# creating a max heap

for i in li:
    heapq.heappush(heap, -i)

# popping the k largest elements
for i in range(k):
    ans.append(-heapq.heappop(heap))

print(ans)
