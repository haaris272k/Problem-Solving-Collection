"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1

"""


def single(nums):
    lst = [i for i in nums if nums.count(i) == 1]
    return lst[0]


nums = list(map(int, input().split()))
print(single(nums))
