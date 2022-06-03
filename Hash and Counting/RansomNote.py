"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false"""


def canConstruct(ransomNote: str, magazine: str) -> bool:

    from collections import Counter

    freq1 = Counter(ransomNote)
    freq2 = Counter(magazine)
    for k, v in freq1.items():
        if k not in freq2 or freq1[k] > freq2[k]:
            return False

    return True


ransomNote = "a"
magazine = "ba"
print(canConstruct(ransomNote, magazine))
