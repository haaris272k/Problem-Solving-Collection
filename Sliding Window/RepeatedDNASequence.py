"""The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]"""

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

DNA_map = {}
start, end = 0, 0
n = len(s)
window = 10

while end < n:
    if end - start + 1 == window:
        DNA_sequence = s[start : end + 1]
        if DNA_sequence not in DNA_map:
            DNA_map[DNA_sequence] = 1
        else:
            DNA_map[DNA_sequence] += 1
        start += 1
    end += 1
print(DNA_map)

ans = []
for k, v in DNA_map.items():
    if v > 1:
        ans.append(k)
print(ans)
