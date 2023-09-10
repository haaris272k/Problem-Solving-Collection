"""Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters."""


s = "abciiidef"
k = 3


vowel_set = set("aeiou")
vowel_count = 0
vowel_count_list = []

start, end, length = 0, 0, len(s)

while end < length:
    # perform calculation
    # precomputation
    if s[end] in vowel_set:
        vowel_count += 1

    # as soon as we hit the window
    if end - start + 1 == k:
        # store vowel count in a list
        vowel_count_list.append(vowel_count)
        # exclude the vowel count which is not in the window
        if s[start] in vowel_set:
            vowel_count -= 1
        start += 1
    end += 1
print(max(vowel_count_list))
