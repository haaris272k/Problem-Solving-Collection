# arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
arr = [1, 2, 3, 4, 5]
d = 2

# Approach 1
# TC: O(n)
# SC: O(n)
# to elements of array to the left/anit-clockwise dir by d
# basic approach is to stre the elements which comes after d in a temp array
# and elements from 0th idx to dth idx

temp = []

for i in range(len(arr)):

    temp = arr[d:] + arr[:d]

print(temp)