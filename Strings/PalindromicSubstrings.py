"""Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
"""
# This could be solved via DP in less time complexity. (in around 1/4th of the time)

s = "a"

substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
count = 0
for i in substrings:
    if i == i[::-1]:
        count += 1
print(count)
