"""Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order."""

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

FreqMap = {}
final_ans = []

words.sort()

for i in words:
    if i in FreqMap:
        FreqMap[i] += 1
    else:
        FreqMap[i] = 1

ans = sorted(FreqMap.items(), key=lambda x: (-x[1], x[0]))


for i in range(k):
    final_ans.append(ans[i][0])
print(final_ans)
