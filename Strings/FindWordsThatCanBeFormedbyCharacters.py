"""You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6."""


words = ["cat", "bt", "hat", "tree"]
chars = "atach"


from collections import Counter

chars_map = Counter(chars)
answer = ""
print(chars_map)
for word in words:
    word_map = Counter(word)
    for character, frequency in word_map.items():
        if chars_map[character] < frequency:
            break
    else:
        print(word)
        answer += word
print(answer)
