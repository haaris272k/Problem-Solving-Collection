"""Given an integer array nums, return an integer array counts where counts[i] 
is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element."""


nums = [5, 2, 6, 1]


# Brute Force
# O(n^2)
# TLE
# ------------------------------#

# size = len(nums)
# answer = []
# for i in range(size):
#     element, count = nums[i], 0
#     for j in nums[i + 1 :]:
#         if j < element:
#             count += 1
#     answer.append(count)
# print(answer)

# ------------------------------#


## Using Binary Search To Find Index
# O(n*logn)
# Accepted

from bisect import bisect_left

size = len(nums)
answer = []
copyArr = nums[:]

copyArr.sort()

for element in nums:
    count = bisect_left(copyArr, element)
    answer.append(count)
    copyArr.remove(copyArr[count])
print(answer)
print(copyArr)
