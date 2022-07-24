"""Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. 
Therefore, we return 6."""


nums = [1, 3, 0, 0, 2, 0, 0, 4]
# nums = [0, 0, 0, 2, 0, 0]
# nums = [2, 10, 2019]

count0 = 0
num0 = 0
for i in range(len(nums)):
    if nums[i] == 0:
        count0 += 1
    else:
        num0 += (count0) * (count0 + 1) // 2
        count0 = 0
if count0:
    num0 += (count0) * (count0 + 1) // 2
print(num0)
