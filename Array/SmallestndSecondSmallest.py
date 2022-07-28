"""Given an array of integers, your task is to find the smallest and second smallest 
element in the array. If smallest and second smallest do not exist, print -1.

Example 1:

Input :
5
2 4 3 5 6
Output :
2 3 
Explanation: 
2 and 3 are respectively the smallest 
and second smallest elements in the array."""


a = [1, 1, 1, 1]


# Method 1:
# TC: O(n*log(n))
# SC: O(1)
tosetlist = list(set(a))
tosetlist.sort()
if len(tosetlist) <= 1:
    print([-1, -1])
else:
    print([tosetlist[0], tosetlist[1]])


# Method 2
# TC: O(n)
# SC: O(1)
if len(set(a)) <= 1:
    print([-1, -1])
else:
    currmin = min(a)
    secondsmallest = max(a)
    for i in a:
        if i > currmin and i < secondsmallest:
            secondsmallest = i
    print(currmin, secondsmallest)
