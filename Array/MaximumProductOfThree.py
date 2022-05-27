"""Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6"""

# Brute Force
nums = [1, 2, 3, 4]
product = 1
product_list = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            product_list.append(nums[i] * nums[j] * nums[k])
print(max(product_list))

# Optimised
import math

if len(nums) == 3:
    print(math.prod(nums))
else:
    nums.sort()
    print(max((nums[0] * nums[1] * nums[-1]), (nums[-1] * nums[-2] * nums[-3])))
