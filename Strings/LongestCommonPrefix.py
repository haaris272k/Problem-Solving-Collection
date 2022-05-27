"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]
strs.sort()
sfirst = strs[0]
slast = strs[-1]
prefix = []
for i in range(len(sfirst)):
    if sfirst[i] == slast[i]:
        prefix.append(sfirst[i])
    else:
        break
print("".join(prefix))
