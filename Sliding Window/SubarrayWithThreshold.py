"""Given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. 
All other sub-arrays of size 3 have averages less than 4 (the threshold)."""


arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5

# subarray with size k and average>=threshold
start, end = 0, 0
c = 0
sum = 0
while end < len(arr):
    sum = sum + arr[end]
    print(sum)
    if end - start + 1 == k:
        if sum / k >= threshold:
            c += 1
        sum = sum - arr[start]
        start += 1
    end += 1
print(c)
