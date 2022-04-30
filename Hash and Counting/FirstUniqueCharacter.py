"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0"""

s = "leeetcode"
from collections import Counter

ans = []
freq = Counter(s)
for k, v in freq.items():
    if v == 1:
        ans.append(k)
if not ans:
    print("-1")
else:
    non_repeating = ans[0]
    print(s.index(non_repeating))
