"""Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds."""


arr = [1, 1, 2, 1, 1]

map = {}

for i in range(len(arr)):
    if arr[i] % 2 != 0:
        map.update({i: arr[i]})

print(map)

keys = list(map.keys())

print(keys)

for i in range(len(keys) - 2):

    idx1 = keys[i]
    idx2 = keys[i + 1]
    idx3 = keys[i + 2]

    if idx3 - idx2 == 1 and idx2 - idx1 == 1:
        print(True)
        break
else:
    print(False)
