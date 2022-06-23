"""Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.

Note: No two strings are the second most repeated, there will be always a single string.

Example 1:

Input:
N = 6
arr[] = {aaa, bbb, ccc, bbb, aaa, aaa}
Output: bbb
Explanation: "bbb" is the second most 
occurring string with frequency 2."""

from collections import OrderedDict

arr = ["geek", "for", "geek", "for", "geek", "aaa"]
freqMap = OrderedDict()
for i in arr:
    if i in freqMap:
        freqMap[i] += 1
    else:
        freqMap[i] = 1
print(freqMap)

sorting = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)
print(sorting[1][0])
