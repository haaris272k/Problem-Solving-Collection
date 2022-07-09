"""Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7]."""

low = 3
high = 7
count = 0
if low % 2 != 0 and high % 2 != 0:
    count = ((high - low + 1) // 2) + 1
else:
    count = (high - low + 1) // 2
print(count)
