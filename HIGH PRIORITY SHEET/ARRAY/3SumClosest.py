"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


nums = [-1, 2, 1, -4]
target = 1


# finding the closest number to the target, the summ should not be equal to the target
mp = {}
n = len(nums)
nums.sort()
for i in range(n - 2):
    left, right = i + 1, n - 1
    while left < right:
        summ = nums[i] + nums[left] + nums[right]

        # Case 1 - if the summ is equal to the target
        # Then it's quite obvious that we have found the closest triplet (the target itself)
        if summ == target:
            print(summ)
            exit()
        # Case 2 - if the summ is less than the target (just like standard 3sum)
        # move the left pointer to the right
        elif summ < target:
            left += 1
        # Case 3 - if the summ is greater than the target (just like standard 3sum)
        # move the right pointer to the left
        else:
            right -= 1

        # keep on updating the closest summ
        # its quite obvious that the closest summ will be the one,
        # which is closest to the target (i.e. the abs difference between the summ and the target is minimum)
        abs_diff = abs(summ - target)
        mp[abs_diff] = summ
print(mp)
closest = min(mp.keys())
print(mp[closest])
