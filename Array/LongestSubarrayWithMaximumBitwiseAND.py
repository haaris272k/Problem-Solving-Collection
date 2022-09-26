"""You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2."""


nums = [1, 2, 3, 3, 2, 2]

n = len(nums)
mx = max(nums)
subarr_length = 0
result = []

""" 
maximum bitwise AND of any subarray would be maximum value of array
bitwise AND will be decreased if element will value lesser than maximum value is included
in subarray, so our objective should be to find maximum subarray consisting of maximum value of array
Basically, our main goal will be to find the maximum length subarray whose max 
value is equal to the max value of the original array (nums)
"""

for i in range(n):
    if nums[i] == mx:
        subarr_length += 1
        result.append(subarr_length)
    else:
        subarr_length = 0
print(result)
print(max(result))
