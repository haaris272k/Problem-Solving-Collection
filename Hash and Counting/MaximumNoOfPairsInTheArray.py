"""You are given a 0-indexed integer array nums. In one operation, you may do the following:

Choose two integers in nums that are equal.
Remove both integers from nums, forming a pair.
The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.

 

Example 1:

Input: nums = [1,3,2,1,3,2,2]
Output: [3,1]
Explanation:
Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums."""


from collections import Counter

# nums = [0]
# nums=[0,1,2,3,4,5,6,7,8,9]
nums = [1, 1, 2, 3, 2, 3, 2]
freq = Counter(nums)

pairs = 0
leftover = 0

for k, v in freq.items():
    if v % 2 == 0:
        pairs += v // 2
    elif v % 2 != 0 and v > 1:
        pairs += v // 2
        leftover += 1
    else:
        leftover += 1
print([pairs, leftover])
