"""Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4]."""

nums = [[7, 34, 45, 10, 12, 27, 13], [27, 21, 45, 10, 12, 13]]
n_of_lists = len(nums)
hmap = {}
ans = []
for i in range(len(nums)):
    for j in range(len(nums[i])):
        if nums[i][j] in hmap:
            hmap[nums[i][j]] += 1
        else:
            hmap[nums[i][j]] = 1
for k, v in hmap.items():

    if v == n_of_lists:

        ans.append(k)
print(sorted(ans))
