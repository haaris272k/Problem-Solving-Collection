"""Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."""


import collections


nums = [1, 1, 1, 2, 2, 3]

# Solution 1
# TC: O(n*2) ~= O(n)
# SC: O(n)

ans = []
freqMap = collections.Counter(nums)

for k, v in freqMap.items():
    if v > 1:
        for i in range(2):
            ans.append(k)
    else:
        ans.append(k)
print(ans)
print(len(ans))

# Solution 2
# TC: O(n)
# SC: O(n)

freqMap = collections.Counter(nums)

# to store the index of the next unique element
i = 0
for k, v in freqMap.items():
    # if the frequency is greater than 1 then we need to add it
    # twice in the array and increment the index by 2
    if v > 1:
        nums[i] = k
        nums[i + 1] = k
        i += 2
    # if the frequency is 1 then we need to add it once in the array
    # and increment the index by 1
    else:
        nums[i] = k
        i += 1
print(nums[:i])
