"""Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing).

Example 1:

Input:
N = 7, x = 0 
arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less 
than 0 is found. So output 
is "-1"."""


A = [1, 2, 8, 10, 11, 12, 19]
N = 7
X = 5
low = 0
high = N - 1
temp = -1
while low <= high:
    mid = low + (high - low) // 2
    if A[mid] == X:
        print(mid)
        break

    elif A[mid] < X:
        temp = mid
        low = mid + 1

    else:
        high = mid - 1
print(temp)
