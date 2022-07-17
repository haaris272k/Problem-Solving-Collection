# LC 307
# Naive solution
# TLE with O(N)


class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        # replacing the element at index with val
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        self.sum = 0
        for i in range(self.left, self.right + 1):
            self.sum += self.nums[i]
        return self.sum


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
index, val = 1, 2
left, right = 0, 2
obj = NumArray(nums)
obj.update(index, val)
param_2 = obj.sumRange(left, right)
print(nums)
print(param_2)
