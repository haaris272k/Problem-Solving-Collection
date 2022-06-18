"""A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz"."""


s = "aababcabc"

# Brute Force
c = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        substring = s[i : j + 1]
        if len((substring)) == 3 and len(set(substring)) == len(substring):
            c += 1
print(c)

# Better Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
# window = 3
# count = 0
# for i in range(len(s) - window + 1):
#     if len(set(s[i : i + window])) == window:
#         count += 1
# print(count)
