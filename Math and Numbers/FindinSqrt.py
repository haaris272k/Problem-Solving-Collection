"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2


"""


def sqroot(x):
    if x == 0 or x == 1:
        return x
    k = 1
    r = 1
    while r <= x:
        k += 1
        r = k * k
    return k - 1


x = int(input())
print(sqroot(x))
