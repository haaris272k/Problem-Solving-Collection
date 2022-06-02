"""You are given an array arr[] of N integers including 0.
The task is to find the smallest positive number missing from the array.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6."""


arr = [0, -10, 1, 3, -20]
arr.sort()  # sorting the array because we need to find the smallest positive number missing
temp = 1  # temp is the smallest positive number missing
n = len(arr)
for i in range(n):
    if (
        arr[i] > 0 and temp == arr[i]
    ):  # if the number is positive and the number is equal to the temp
        temp += 1

print(temp)
