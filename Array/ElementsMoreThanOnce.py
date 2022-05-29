"""
Given an array a[] of size N which contains elements from 0 to N-1,
you need to find all the elements occurring more than once in the given array.

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: -1
Explanation: N=4 and all elements from 0
to (N-1 = 3) are present in the given
array. Therefore output is -1.

"""

a = list(map(int, input().strip().split()))
dup = []
original = []
for i in a:
    if i not in original:
        original.append(i)
    else:
        dup.append(i)
if len(dup) != 0:
    for ele in dup:
        print(ele, end=" ")
else:
    print("-1")
