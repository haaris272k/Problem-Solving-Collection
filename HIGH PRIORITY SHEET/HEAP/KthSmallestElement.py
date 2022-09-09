"""
Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Example 1:

Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.

"""

from heapq import heapify
import heapq


arr = [7, 10, 4, 3, 20, 15]
k = 3

# Method 1: Sort the array and return the kth element
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
arr.sort()
print(arr[k - 1])


# Method 2: Use a min heap
# Time Complexity: O(nlogk)
# Space Complexity: O(k)

ans = []
heapify(arr)
for i in range(k):
    ans.append(heapq.heappop(arr))
print(ans[k - 1])
