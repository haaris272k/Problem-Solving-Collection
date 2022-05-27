'''A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

 

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"'''

# word = "aeiouu"
# substrings = []
# c = 0
# for i in range(len(word)):
#     for j in range(i + 1, len(word) + 1):
#         substrings.append(word[i:j])

# vowels_set = {"a", "e", "i", "o", "u"}
# for i in range(len(substrings)):
#     if set(substrings[i]) == vowels_set:
#         c += 1
# print(c)

word = "0110111"
substrings = []
c = 0
for i in range(len(word)):
    for j in range(i + 1, len(word) + 1):
        substrings.append(word[i:j])
vowels_set = {"1"}
for i in range(len(substrings)):
    if set(substrings[i]) == vowels_set:
        c += 1
print(c)
