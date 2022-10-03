"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4"""


def search(arr, l, h, key):

    while l <= h:
        mid = (l + h) - l // 2
        if arr[mid] == key:
            return mid

        # If arr[l...mid] is sorted
        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if arr[l] <= arr[mid]:
            # basic binary search logic
            if key <= arr[l] and key <= arr[mid]:
                # if mid is smaller than equal to key then so, decrease the high pointer
                return search(arr, l, mid - 1, key)
            else:
                # if mid is smaller than equal to key then so, increase the low pointer
                return search(arr, mid + 1, h, key)

        # If arr[l..mid] is not sorted, then arr[mid... r]
        # must be sorted
        else:
            # basic binary search logic
            if key >= arr[l] and key >= arr[mid]:
                # if mid is smaller than equal to key then so, increase the low pointer
                return search(arr, mid + 1, h, key)
            # if mid is smaller than equal to key then so, decrease the high pointer
            return search(arr, l, mid - 1, key)


arr = [3, 4, 5, 1, 2]
n = len(arr)
key = 11
l, h = 0, n - 1


if search(arr, l, h, key) is None:
    print(-1)
else:
    print(search(arr, l, h, key))
