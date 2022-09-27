"""
Binary Search Algorithm
TC: O(log n)

"""

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
low = 0
high = len(nums) - 1
for i in range(len(nums)):

    mid = low + (high - low) // 2

    if nums[mid] == target:

        print(mid)

    elif nums[mid] < target:

        low = mid + 1
    else:
        high = mid - 1
else:
    print(-1)
