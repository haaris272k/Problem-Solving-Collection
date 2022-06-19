"""Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.

 

Example 1:

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case."""

s = "lEeTcOdE"
ans = []
for i in range(len(s)):
    if s[i].islower():
        letter = s[i]
        if letter.upper() in s:
            ans.append(letter.upper())
ans.sort()
if ans:
    print(ans[-1])
else:
    print("")
