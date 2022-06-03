"""There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

 

Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken."""


text = "hello world"
brokenLetters = "ad"
text_lst = text.split()
char_list = list(brokenLetters)
word = []

for i in range(len(text_lst)):

    for j in char_list:

        if j in text_lst[i]:
            word.append(text_lst[i])

print(abs(len(text_lst) - len(word)))
