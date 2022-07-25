"""Given a string containing lower and uppercase alphabets, the task is to find the maximum number of characters between any two same character in the string.

Example 1:

Input:
S = "socks"
Output: 3
Explanation: There are 3 characters between
the two occurrences of 's'."""

# s = "socks"
# s = "FoR"
s = "IeFzIkavsEZyxXLgpfdOe"
idxlist = []
distlist = []
repeatingchar = [i for i in s if s.count(i) > 1]
print(repeatingchar)
if repeatingchar:
    repeatingchar = set(repeatingchar)
    for a, b in enumerate(s):

        if b in repeatingchar:

            idxlist.append(a)
    print(idxlist)
    for dist in range(len(idxlist)):
        # subtracting the distance from all the distances
        distlist.append(abs(idxlist[dist] - idxlist[dist - 1]) - 1)
    print(distlist)
    print(max(distlist))

else:
    print(-1)
