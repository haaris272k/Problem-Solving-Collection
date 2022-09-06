"""Given two sorted arrays of size m and n respectively, you are tasked with finding the element that would be at the kth position of the final sorted array.

Input: m = 5
       n = 4
       array1 = [2,3,6,7,9]
       array2 = [1,4,8,10]
       k = 5"""

# Brute Force
array1 = [2, 3, 6, 7, 9]
array2 = [1, 4, 8, 10]
k = 5
array1.extend(array2)
array1.sort()
print(array1[k - 1])
