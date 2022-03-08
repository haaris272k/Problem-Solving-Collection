"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]



"""


"""inefficient approach"""
# nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = list(map(int, input().split()))
l = len(nums)
nos = []
for i in range(1, l + 1):
    if i not in nums:
        nos.append(i)
print(nos)


"""efficient approach"""
# nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = list(map(int, input().split()))

n = len(nums)
nums2 = [i for i in range(1, n + 1)]
print(set(nums2).difference(nums))
