"""Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3."""


nums = [1, 1, 0, 1, 1, 1]
c = 0
lst = []

for i in range(0, len(nums)):
    if nums[i] == 1:
        c += 1
        lst.append(c)

    else:
        c = 0

if len(lst) == 0:
    print(0)
else:
    print(max(lst))
