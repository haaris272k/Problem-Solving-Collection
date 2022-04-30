"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]"""

# TC O(n)
# approach using count (c)
nums = [3, 3, 4, 4, 4, 3]
target = 3

positions = []
c = 0

for single_index in range(len(nums)):
    if nums[single_index] == target:
        c += 1

if c == 0:
    print([-1, -1])
elif c == 1:
    ind = nums.index(target)
    print([ind, ind])
else:
    for elements in range(len(nums)):
        if nums[elements] == target:
            positions.append(elements)
    print([positions[0]] + [positions[-1]])
