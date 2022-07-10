"""The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only."""


s = "leetcode"
previous = s[0]
count = 0
maxi = 0

for i in s:
    if i == previous:
        count += 1
    else:
        previous = i
        count = 1
    maxi = max(maxi, count)
print(maxi)
