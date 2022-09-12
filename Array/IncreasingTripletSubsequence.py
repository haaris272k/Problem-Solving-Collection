nums = [5, 4, 3, 2, 1]
# nums = [1, 2, 3, 4, 5]
# nums = [2, 1, 5, 0, 4, 6]
# nums = [20, 100, 10, 12, 5, 13]

"""Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid."""

n = len(nums)
first = second = float("inf")
for i in range(n):
    if nums[i] < first:
        print("first", first)
        first = nums[i]
    elif nums[i] < second:
        print("second", second)
        second = nums[i]
print(first, second)
