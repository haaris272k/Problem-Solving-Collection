"""Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2."""

nums1 = [1, 3]
nums2 = [2]

# Sorting + Bruteforce

new_nums = sorted(nums1 + nums2)
l = len(new_nums)
p = int(l / 2)
if (l & 1) == 1:
    print(new_nums[p])
else:
    print((new_nums[p] + new_nums[p - 1]) / 2)
