"""Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3."""

s = "abcabcbb"
# Method 1: Sliding window
myset = set()
start = 0
res = []
n = len(s)
try:
    for end in range(n):
        while s[end] in myset:
            myset.remove(s[start])
            start += 1
        myset.add(s[end])
        res.append(len(myset))
    print(res)
    print(max(res))
except:
    print(0)
