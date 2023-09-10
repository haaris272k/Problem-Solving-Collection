"""Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Powerset will have 2**n elements, where n is the number of elements in nums."""

nums = [1, 2, 3]
n = len(nums)
result = [[nums[k] for k in range(n) if i & 1 << k] for i in range(2 ** n)]
print(result)
