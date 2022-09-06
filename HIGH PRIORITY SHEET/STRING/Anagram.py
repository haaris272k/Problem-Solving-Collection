"""

Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not.
An anagram of a string is another string that contains the same characters, only the order of characters can be different.
For example, act and tac are an anagram of each other.

Example 1:

Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have samecharacters with
        same frequency. So, both are anagrams.
        
"""


def isAnagram(a, b):
    if sorted(a) == sorted(b):
        return True
    return False


a, b = input("Enter string 1 "), input("Enter string 2 ")
print(isAnagram(a, b))
