"""Given an unsorted array arr[] and two numbers x and y,
find the minimum distance between x and y in arr[].
The array might also contain duplicates.
You may assume that both x and y are different and present in arr[].

Examples: 

Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 
and 2 is 1.
Explanation: 1 is at index 0 and 2 is at 
index 1, so the distance is 1"""


arr = [86, 39, 90, 67, 84, 66, 62]
x, y = 42, 12
# arr = [1, 2, 3, 2]
# x, y = 1, 2

min_dist = 100000  # taking an infinite value
idx_x, idx_y = -1, -1  # initializing the indices as -1
n = len(arr)

for i in range(n):
    # if the current element is equal to x
    # then update the index of x
    if arr[i] == x:
        idx_x = i
    # if the current element is equal to y
    # then update the index of y
    elif arr[i] == y:
        idx_y = i
    # find min dist if both x and y are present and not equal to -1
    if idx_x != -1 and idx_y != -1:
        min_dist = min(min_dist, abs(idx_x - idx_y))
print(min_dist)
