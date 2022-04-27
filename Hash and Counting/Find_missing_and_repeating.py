"""

Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.



"""
from collections import Counter


def missndrepeat(arr, n):

    dup_num = []

    freq = Counter(arr)

    for k, v in freq.items():

        if v == 2:

            dup_num.append(k)

            break

    sum_natural = (n * (n + 1)) // 2

    sum_arr = sum(set(arr))

    missing_num = [sum_natural - sum_arr]

    return dup_num + missing_num


arr = list(map(int, input().split()))

n = len(arr)

print(missndrepeat(arr, n))
