"""You are given two strings s1 and s2 of equal length. 
A string swap is an operation where you choose two indices in 
a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing 
at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank"."""


s1 = "bank"
s2 = "kanb"

if s1 == s2:
    # return True
    print(True)

s1_chars = sorted(s1)
s2_chars = sorted(s2)
print(s1_chars, s2_chars)
if s1_chars != s2_chars:
    # return False
    print(False)

checklist = list(s1)
num_mismatches = 0
for i in range(len(s2)):
    if s2[i] != checklist[i]:
        num_mismatches += 1

print((num_mismatches == 0) or (num_mismatches == 2))
