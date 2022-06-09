"""Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted."""


def sortArrayByParityII(nums: list[int]) -> list[int]:
    even_ele = [i for i in nums if i % 2 == 0]
    odd_ele = [i for i in nums if i % 2 != 0]
    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = even_ele[i // 2]
        else:
            nums[i] = odd_ele[i // 2]
    return nums


nums = [4, 2, 5, 7]
print(sortArrayByParityII(nums))
