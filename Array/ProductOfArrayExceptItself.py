"""Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]"""


# nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]

"""Approach 1 (Simple Brute Force)"""
# Time Complexity: O(n^2)
# ans = []
# def product(nums):
#     prod = 1
#     for i in nums:
#         prod *= i
#     return prod
# for i in range(len(nums)):
#     Arrexceptnum = nums[:i] + nums[i + 1 :]  # forming array except the current number
#     ans.append(product(Arrexceptnum))
# print(ans)

"""Approach - 2 (Using map) 
The idea is to store the product in a map,where key would be the element which was excluded 
and value would be the product computed except the key. It will save the computational time
in the case when there will be duplicates so, in that case we would not have to compute the
product again and again.ex [9,9,9,9,9,9,9] This is the best case and our code would be
efficient than the case where we would have unqiue elements"""

# TC - O(n) SC - O(n)
# TC - O(n^2) (Worst case) SC - O(n)
# import math
# nums = [1, 2, 3, 4]
# answer, lookup = [], {}
# for idx in range(len(nums)):
#     num = nums[idx]
#     if num not in lookup:
#         lookup[num] = math.prod(nums[:idx] + nums[idx + 1 :])
#         print(lookup)
#     answer.append(lookup[num])
# print(answer)
