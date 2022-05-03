"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1

"""

"""The digital root of a positive integer is found by summing the digits of the integer. If the resulting value is a single digit then that digit is the digital root. If the resulting value contains two or more digits, those digits are summed and the process is repeated.
This is continued as long as necessary to obtain a single digit. So, in this question we have to find the digital root of a number."""


def digitalRoot():
    num = 11
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9


print(digitalRoot())
