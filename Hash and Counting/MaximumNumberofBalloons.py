"""Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2"""


import collections


text = "nlaebolko"
# text = "loonbalxballpoonbaloon"
# text = "leetcode"
# text = "balon"
word = "balloon"

map1 = collections.Counter(text)
map2 = collections.Counter(word)
print(min(map1[i] // map2[i] for i in map2))
