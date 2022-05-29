"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true

Example 2:

Input: n = 0
Output: false


"""


def power(n):
    for i in range(0, n):
        if 3 ** i > n:
            return False
        if 3 ** i == n:
            return True


n = int(input())
print(power(n))
