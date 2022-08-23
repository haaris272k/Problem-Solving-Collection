"""Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


Example 1:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray."""

# Brute Force Solution:
# Our goal is to find the subarray with the maximum sum.
# As we could easily see that It is less efficient
arr = [1, 2, 3, -2, 5]
subarray = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        subarray.append(arr[i : j + 1])
print(
    "The subarray with maximum sum is",
    max(subarray, key=sum),
    "with sum",
    sum(max(subarray, key=sum)),
)

# Kadane's Algorithm:
# We can use Kadane's algorithm to find the subarray with the maximum sum,efficiently.
# TC is O(n)
maxi = arr[0]
curr_maxi = arr[0]
n = len(arr)
for i in range(1, n):
    curr_maxi = max(arr[i], curr_maxi + arr[i])
    maxi = max(maxi, curr_maxi)
print(maxi)
