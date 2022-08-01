"""Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to 
b and a is equal to d. For example, (10, 20) and (20, 10) are symmetric.
Given an array of pairs find all symmetric pairs in it. 
It may be assumed that the first elements of all pairs are distinct.
Example: 

Input: arr[] = {{11, 20}, {30, 40}, {5, 10}, {40, 30}, {10, 5}}
Output: Following pairs have symmetric pairs
        (30, 40)
        (5, 10)"""
a = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]

# Brute Force Solution
# c = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i][0] == a[j][1] and a[i][1] == a[j][0]:
#             c += 1
#             print("pairs :", a[i], a[j])
# print(c)


# TC: O(n^2)

map = {}
# if a==d and b==c
c = 0
for i in range(len(a)):
    first = a[i][0]
    second = a[i][1]
    print(map.keys(), map.values())
    if first in map.keys() and second in map.values():

        c += 1
    else:
        map[first] = second
        map[second] = first
print(c)
print(map)
