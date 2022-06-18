"""A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5)."""


import math

n = 10
numbers = list(range(1, n + 1))
c = 0
ans = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        sqroot = math.sqrt(numbers[i] ** 2 + numbers[j] ** 2)
        # checking if squreoot is <=n or not
        if int(sqroot) == sqroot and sqroot <= n:
            c += 1
print(c * 2)
