"""Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer."""


# s = "tree"
# s = "cccaaa"
s = "Aabb"
from collections import Counter
import heapq

string = ""
FreqMap = Counter(s)
# sorting string on the basis of decreasing frequency
FreqMap = sorted(FreqMap.items(), key=lambda x: x[1], reverse=True)
print(FreqMap)
for i in FreqMap:
    string += i[0] * i[1]
print(string)
