"""A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]"""


def isselfdividing(n):

    selfdividing = True

    if n > 1 and n <= 9:
        return True

    elif "0" in str(n):
        return False

    digits = []
    for i in str(n):
        digits.append(int(i))

    for i in digits:
        if n % i != 0:
            selfdividing = False
    return selfdividing


def solution(left, right):
    lst = []
    for i in range(left, right + 1):
        if isselfdividing(i):
            lst.append(i)
    return lst


left = 1
right = 22
print(solution(left, right))
