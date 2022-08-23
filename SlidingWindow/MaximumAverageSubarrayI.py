"""You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75"""


# using sliding window to find max average subarray salary of size k
# Method 1 (Quite slow)
def max_avg_subarray(nums, k):
    sum_of_k = 0
    all_sums = []
    start, end = 0, 0
    while end < len(nums):
        if end - start + 1 == k:
            # finding sum of k elements
            sum_of_k += nums[end]
            all_sums.append(sum_of_k)
            sum_of_k -= nums[start]
            start += 1
            end += 1
        else:
            sum_of_k += nums[end]
            end += 1
    return ("Ans using method 1", max(all_sums) / k)


nums = [7, 4, 5, 8, 8, 3, 9, 8, 7, 6]
k = 7
print(max_avg_subarray(nums, k))


# using sliding window to find max average subarray salary of size k
# Method 2 (slight difference in TC)
def max_avg_subarray(nums, k):

    n = len(nums)
    # Computing sum of first window of size k
    window_sum = sum(nums[:k])

    # making it current max as it is the only available sum of 1st window of size k
    max_sum = window_sum

    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)

    # finally finding max average
    # It's quite obvious that max sum would result in the max average
    # that is the reason we put focus on finding the max sum
    return ("Ans using method 2 is ", max_sum / k)


nums = [7, 4, 5, 8, 8, 3, 9, 8, 7, 6]
k = 7

print(max_avg_subarray(nums, k))
