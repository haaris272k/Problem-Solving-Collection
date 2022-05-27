"""You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 

Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling"""


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
map = {}
for i in range(len(s)):
    map[indices[i]] = s[i]
    # mapping indices to the characters
    # If char would have been keys then the duplicate values would have been ignored

ans = ""
sorted_indices = sorted(map.keys())
# once the mapping is done, sort the keys that is index and append char which is associated to that index in the map
for i in sorted_indices:
    ans += map[i]  # appending each char associated to that specific index
print(ans)
