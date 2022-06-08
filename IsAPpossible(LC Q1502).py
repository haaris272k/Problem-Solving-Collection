"""A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements 
is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
Otherwise, return false.

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively,
between each consecutive elements."""


# as we know that AP series is always in increasing order
# in this q we just we have to check whether the difference between consecutive elements is same or not
# if array is sorted then we can check the difference between consecutive elements
# else we can sort the array and check the difference between consecutive elements

arr = [1, 2, 4]
n = len(arr)
arr.sort()
diff = arr[1] - arr[0]
for i in range(n - 1):

    if arr[i + 1] - arr[i] != diff:
        print(False)
        break
else:
    print(True)
