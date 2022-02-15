"""
Given a string str. The task is to find the maximum occurring character in the string str.
If more than one character occurs the maximum number of time then print the lexicographically smaller character.

Example 1:

Input:
str = testsample
Output: e
Explanation: e is the character which
is having the highest frequency.
"""

from collections import Counter

a = input()
freq = Counter(a)
maximum = max(freq.values())
sorting_res = sorted(freq.items())
for i, j in sorting_res:
    if j == maximum:
        print(i)
        break
