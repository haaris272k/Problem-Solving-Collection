"""You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

Sort the values at odd indices of nums in non-increasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
Sort the values at even indices of nums in non-decreasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
Return the array formed after rearranging the values of nums.

 

Example 1:

Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation: 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1]."""

# Selection Sort
# Time: O(n^2)
# Space: O(1)
nums = [4, 1, 2, 3]
n = len(nums)
for i in range(n):

    for j in range(i + 1, n):

        if i % 2 == 0 and j % 2 == 0:

            if nums[i] > nums[j]:

                nums[i], nums[j] = nums[j], nums[i]

        elif i % 2 != 0 and j % 2 != 0:

            if nums[i] < nums[j]:

                nums[i], nums[j] = nums[j], nums[i]
        else:

            continue

print(nums)
