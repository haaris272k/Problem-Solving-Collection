"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]"""


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
map = {}
ans = []


sorted_strs = ["".join(sorted(x)) for x in strs]

for i in range(len(strs)):

    if sorted_strs[i] not in map:

        map[sorted_strs[i]] = [strs[i]]

    else:
        map[sorted_strs[i]].append(strs[i])

for key in map:

    ans.append(map[key])

print(ans)
