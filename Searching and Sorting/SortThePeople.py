"""You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John."""


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]

# using map
n = len(names)
height_names = {}
for i in range(n):
    height_names[heights[i]] = names[i]

heights.sort(reverse=True)
ans = []
for i in range(n):
    ans.append(height_names[heights[i]])
print(ans)
