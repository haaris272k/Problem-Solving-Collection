# This Question was asked in Rakuten Singapore's OA
# a word is well-structured if it:
# 1. starts with a consonant
# 2. does not contain two consecutive vowels
# 3. does not contain two consecutive consonants

# task is to find the number of well-structured words that can be obtained by rearranging the letters of s

# s='BAR'
# s='AABB'
# s='AAAB'
s='AABCY'

# constants and variables
starts_with_consonant = True
contains_two_consecutive_vowels = True
contains_two_consecutive_consonants = True
modudlo=10**9+7

# function to check if a character is a vowel
def is_vowel(c):
    if c in ['A','E','I','O','U']:
        return True
    else:
        return False

# function to check if a character is a consonant
def is_consonant(c):
    if c in ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']:
        return True
    else:
        return False

# function to check if a word is well-structured or not
def iswellstructured(s):
    if is_consonant(s[0]):
        if len(s)>1:
            for i in range(1,len(s)):
                if is_vowel(s[i-1]) and is_vowel(s[i]):
                    return False
                if is_consonant(s[i-1]) and is_consonant(s[i]):
                    return False
        return True
    else:
        return False


# finding rearrangements of s and passing them to iswellstructured function
# if the word is well-structured, incrementing count by 1
from itertools import permutations
perms = set([''.join(p) for p in permutations(s)])
count=0
for word in perms:
    if iswellstructured(word):
        count+=1
print(count%modudlo)

