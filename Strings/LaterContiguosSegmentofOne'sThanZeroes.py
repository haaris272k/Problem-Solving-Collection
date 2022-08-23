"""Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

 

Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true."""

s = "1101"
longest_zero = 0
longest_one = 0

sequened_one = []
sequened_zero = []

for i in range(len(s)):
    if s[i] == "1":
        longest_one += 1
    else:
        longest_one = 0
    if s[i] == "0":
        longest_zero += 1
    else:
        longest_zero = 0
    sequened_one.append(longest_one)
    sequened_zero.append(longest_zero)
print(sequened_one)
print(sequened_zero)

if max(sequened_one) > max(sequened_zero):
    print(True)
else:
    print(False)
