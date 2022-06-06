"""You are given a 0-indexed integer array nums whose length is a power of 2.

Apply the following algorithm on nums:

Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the last number that remains in nums after applying the algorithm.

 

Example 1:


Input: nums = [1,3,5,2,4,8,2,2]
Output: 1
Explanation: The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1."""

nums = [70, 38, 21, 22]
if len(nums) == 1:
    print(nums[0])  # This is the base case as specified in the problem
else:

    while len(nums) != 1:  # repating the process till we get length 1
        new_nums = []
        # Algorithm is directly from the problem statement
        for i in range(0, len(nums) // 2):
            if i % 2 == 0:
                new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
            else:
                new_nums.append(max(nums[2 * i], nums[2 * i + 1]))
        nums = new_nums
    print(nums[0])  # accesss the element from the array
