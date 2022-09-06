"""You are given a sorted array consisting of only integers 
where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2"""

# Approach - 1 : Using hashtable
# Time Complexity - O(n)
# Space Complexity - O(n)

nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

from collections import Counter

dicc = Counter(nums)

for k, v in dicc.items():

    if v == 1:

        print(k)

# Approach - 2 : Using binary search
