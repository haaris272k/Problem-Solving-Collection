"""You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike."""


s = "MerryChristmas"
n = len(s)
c1 = 0
c2 = 0
first_half = s[: n // 2]
second_half = s[n // 2 :]
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for i in first_half:
    if i in vowels:
        c1 += 1
for j in second_half:
    if j in vowels:
        c2 += 1
print(c1, c2)
