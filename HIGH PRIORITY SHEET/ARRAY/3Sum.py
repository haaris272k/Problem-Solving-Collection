"""
Variant - 1 (Original Leetcode 15)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

# -------------------------------------------------------------------------------------------#

nums = [-1, 0, 1, 2, -1, -4]

n = len(nums)

# sort the array
nums.sort()

# iterate upto n-2
for i in range(n - 2):

    # take two pntrs left and right
    # left will be i+1 and right will be n-1 means left will run from 1 index more than i and,
    # right will run from last index upto i+1 index

    left, right = i + 1, n - 1

    # iterate till left is less than right
    while left < right:

        # if sum of nums[i], nums[left] and nums[right] is 0 then print the triplet
        if nums[i] + nums[left] + nums[right] == 0:
            print(nums[i], nums[left], nums[right])
            left += 1
            right -= 1

        # if sum is less than 0 then increment left
        elif nums[i] + nums[left] + nums[right] < 0:
            left += 1

        # if sum is greater than 0 then decrement right
        else:
            right -= 1

# -------------------------------------------------------------------------------------------#


"""
Variant - 2 (Gfg)
Everything is same as above except we have to return 1 if triplet is found else 0
"""

"""
Variant - 3 (Gfg)
Everything is same as above except we have to count the number of triplets with sum 0
"""

""" 
Variant - 4 (Gfg)
Everything is same as above except we have to find 3 numbers with sum == target (any target)
"""
