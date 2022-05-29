nums = [1, 2, 3, 4]
new_nums = [0] * len(nums)  # initialize a new list with the same length as nums
for i in range(len(nums)):
    new_nums[i] = new_nums[i - 1] + nums[i]
print(new_nums)
