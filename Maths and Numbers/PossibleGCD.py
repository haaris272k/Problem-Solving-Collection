"""Chef has two distinct positive integers A and B.

Chef wonders how many distinct values are possible for the expression gcd(A+X,B+X), where X can take any non-negative integer value.

Help Chef find this value.

Here, gcd stands for Greatest Common Divisor.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains two distinct space separated integers A and B.

Input
2
1 2 
12 8

Output

1
3

"""


import math

aee, bee = 1, 2

temporary = abs(aee - bee)

limit = int(math.sqrt(temporary))

count = 0
for i in range(1, limit + 1):
    if temporary % i == 0:
        if temporary / i == i:
            count += 1
        else:
            count += 2
print(count)
