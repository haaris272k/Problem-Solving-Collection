"""Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer."""


nums = [1, 2, 1, 3, 2, 5]

# not an optimised sol.
# rtime 5000ms
hashtable = {i: nums.count(i) for i in nums}
ans = []
for i in hashtable:
    if hashtable[i] == 1:
        ans.append(i)
print(ans)


# better sol
# rtime 103 ms
htable = {}
for i in nums:
    if i in htable:
        htable[i] += 1
    else:
        htable[i] = 1
for k, v in htable.items():
    if v == 1:
        print(k)

# use Counter for optimised sol
# rtime 60ms
from collections import Counter

lst = []
freq = Counter(nums)
for i, j in freq.items():
    if j == 1:
        lst.append(i)
print(lst)
