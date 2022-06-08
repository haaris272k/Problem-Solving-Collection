"""Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order."""

arr = [4, 2, 1, 3]
arr.sort()

# mini=float('inf') or # taking large value so as no value gets ignored
mini = 1000000

res = []

for i in range(len(arr) - 1):
    mini = min(mini, arr[i + 1] - arr[i])

for j in range(len(arr) - 1):
    if arr[j + 1] - arr[j] == mini:
        res.append([arr[j], arr[j + 1]])
print(res)
