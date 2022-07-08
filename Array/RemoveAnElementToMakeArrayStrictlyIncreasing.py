"""Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

 

Example 1:

Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true."""

# nums = [1, 1, 1]
nums = [1, 2, 10, 5, 7]


def isIncreasing(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True


def sol(nums):
    for i in range(len(nums)):
        if isIncreasing(nums[:i] + nums[i + 1 :]):
            return True
    return False


print(sol(nums))
