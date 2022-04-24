"""

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

"""


paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
c = [",", ".", "!", "?", "'", ";"]
for i in c:
    paragraph = paragraph.replace(i, " ")
conv = paragraph.lower().split()
hashtable = {i: conv.count(i) for i in conv if i not in banned}
maxi_occurence = max(hashtable.values())
for key, value in hashtable.items():
    if value == maxi_occurence:
        print(key)
