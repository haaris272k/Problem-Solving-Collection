"""You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54."""


nums = [18, 43, 36, 13, 7]
# nums = [10, 12, 19, 14]

# O(n^2)
# TLE
SumList = []
NumsLen = len(nums)
s1, s2 = 0, 0
for i in range(NumsLen):
    for j in range(i + 1, NumsLen):
        if i != j:
            for k in str(nums[i]):
                s1 += int(k)
            for k in str(nums[j]):
                s2 += int(k)
            if s1 == s2:
                SumList.append(nums[i] + nums[j])
            s1, s2 = 0, 0

if SumList:
    print(max(SumList))
else:
    print(-1)
