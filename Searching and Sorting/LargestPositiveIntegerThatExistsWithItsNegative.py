"""Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array."""

nums = [-1, 2, -3, 3]
import heapq

"""Using Sort"""
# Time: O(nlogn)
# Space: O(1)
n = len(nums)
nums.sort()
for i in range(n):
    maxed = nums.pop()
    if -maxed in nums:
        print(maxed)
        break
else:
    print(-1)

"""Using heap"""
# TC: O(nlogn)
# SC: O(n)

max_heap = [-i for i in nums]

heapq.heapify(max_heap)

while max_heap:
    maxed = heapq.heappop(max_heap)
    if -maxed in max_heap:
        # convert back to positive
        print(-maxed)
        break

else:
    print(-1)
