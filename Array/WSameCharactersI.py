""" You are given a String X and a string containing single character Y. 
Your task is to find the largest distance between any two occurrences of the character
Y in string X.

The Distance is defined by the no of distinct characters between any
two occurrences of char Y in string X (Exclude whitespaces).

If there is no occurrences or only one occurrences of the given character,
the function should return -1.

Example:

Input1: my name is ranary

Input2: a

Output: 7"""

s1 = "my name is ranary lmao popalola"
s2 = "a"
s1 = s1.replace(" ", "")  # remove whitespaces

idxlist = []
counts2 = s1.count(s2)

if not counts2 or counts2 == 1:
    print(-1)
else:

    for a, b in enumerate(s1):
        if b == s2:
            idxlist.append(a)
    print(idxlist)
    maxdist, mindist = max(idxlist), min(idxlist)
    print(maxdist - mindist - 1)
