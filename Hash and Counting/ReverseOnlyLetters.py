'''Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"'''


s = "a-bC-dEf-ghIj"
# s = "Test1ng-Leet=code-Q!"


specialmap = {}
newstringlist = []
finalstring = []

# mapping special characters to their corresponding index in the string
for a, b in enumerate(s):
    if not (b.isalpha()):
        if a not in specialmap:
            specialmap[a] = b
        else:
            specialmap[a].append(b)
print(specialmap)


# reverse the string except the special characters
for i in s:
    if i.isalpha():
        newstringlist.append(i)
newstringlist.reverse()
print(newstringlist)

# inserting the special characters in the right order
for i in range(len(s)):
    if i in specialmap:
        newstringlist.insert(i, specialmap[i])
print(newstringlist)

# joining the list to a string
finalstring = "".join(newstringlist)
print(finalstring)
