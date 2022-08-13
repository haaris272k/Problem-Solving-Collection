"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4"""


# ------------------------------------------Logic------------------------------------------#

# The logic is to use perform Binary search on 'two sorted parts'
# i.e. on two different 'sorted parts' of the array as  we know the 'rotation' would result in two 'sorted parts'
# The index of smallest element would serve as a 'pivot' which would be the dividing point for the two sorted arrays
# First perform the BinSearch on the one sorted part then on the other sorted part
# for Part-I start would be 0 and end would be index of element just b4 the minimum element
# for Part-II start would be index of min element and end would be the last index
# Either both of the times we would get -1 which means element is not there in the array else , unique answer

# ------------------------------------------------------------------------------------------#

# Function to Perform Binary Search
def BinSearch(nums, start, end, target, n):

    for i in range(n):
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def solution(nums, target):
    n = len(nums)
    min_idx = nums.index(min(nums))
    start1 = 0
    end1 = min_idx - 1
    start2 = min_idx
    end2 = n - 1

    ans1 = BinSearch(nums, start1, end1, target, n)
    ans2 = BinSearch(nums, start2, end2, target, n)

    if ans1 >= 0 or ans2 >= 0:
        return ans1 if ans1 >= 0 else ans2
    else:
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(solution(nums, target))
