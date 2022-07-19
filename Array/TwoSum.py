"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""


def twosum_map(a, target):
    d = {}
    c = 0
    for i in range(len(a)):
        if target - a[i] in d:
            print(d[target - a[i]], i)
            c += 1
        d[a[i]] = i
    return ""


a = [2, 7, 11, 15, 8, 1]
target = 9
print(twosum_map(a, target))
