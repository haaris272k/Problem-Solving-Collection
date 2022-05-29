"""
Given two arrays A and B contains integers of size N and M, the task is to find numbers which are present in the first array, but not present in the second array.

Example 1:

Input: N = 6, M = 5
A[] = {1, 2, 3, 4, 5, 10}
B[] = {2, 3, 1, 0, 5}
Output: 4 10
Explanation: 4 and 10 are present in 
first array, but not in second array.

"""

from collections import Counter


def findMissing(A, B):

    a = Counter(A)
    b = Counter(B)
    l = []
    for i in A:
        if i not in b.keys():
            l.append(i)
    return l


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(findMissing(A, B))
