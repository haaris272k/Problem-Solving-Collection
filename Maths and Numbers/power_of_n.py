"""
Given an integer n, return true if it is a power of x (x is any number say 4). Otherwise, return false.

An integer n is a power of x, if there exists an integer k such that n == 4k.

"""

""" A generic solution to all the "number is a power of x" checking problems"""


def power(n, x):
    lst = [i for i in range(n) if x ** i == n]
    if lst:
        return True
    return False


n = int(input("Enter the num n "))
x = int(input("Enter the num x "))
print(power(n, x))
