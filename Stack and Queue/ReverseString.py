"""Reverse a string using stack"""

s = "alpha"
toList = list(s)
reverseString = ""
for i in range(len(s)):
    poppedChar = toList.pop()
    reverseString += poppedChar
print(reverseString)
