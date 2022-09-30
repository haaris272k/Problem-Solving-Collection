"""
Binary Search Algorithm
TC: O(log n)

"""

nums = [0, 1, 2, 7, 8, 13, 15]
n = len(nums)
target = 13
l, r = 0, n - 1
for i in range(n):
    mid = (l + r) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] > target:
        r = mid - 1
    else:
        l = mid + 1
