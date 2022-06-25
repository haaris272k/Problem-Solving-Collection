"""You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair."""

# s = "l|*e*et|c**o|*de|"
s = "*||*|||||*|*|***||*||***|"

IndList = []
extractedStrings = []
finalString = ""

# finding the indices of the '|' to extract the characters lying between them
for i in range(len(s)):
    if s[i] == "|":
        IndList.append(i)

# extracting the characters lying between the '|'
for i in range(len(IndList) // 2):
    extracted = s[IndList[i * 2] : IndList[i * 2 + 1]]
    extractedStrings.append(extracted)

# concatenating the extracted characters
for i in range(len(extractedStrings)):
    finalString += extractedStrings[i]

# counting the number of '*' in the final string
print(s.count("*") - finalString.count("*"))
