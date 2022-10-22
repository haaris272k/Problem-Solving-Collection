'''You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.'''

from collections import Counter

s = "leetcode"
t = "practice"
freq_s=Counter(s)
freq_t=Counter(t)

print(freq_s)
print(freq_t)

ans=0
for k,v in freq_t.items():
    #Loop over all characters if the frequency of a character in t is less than the frequency of the same character in s 
    # then add the difference between the frequencies to the answer.
    if freq_s[k]<freq_t[k]:
        ans+=freq_t[k]-freq_s[k]
print(ans)       