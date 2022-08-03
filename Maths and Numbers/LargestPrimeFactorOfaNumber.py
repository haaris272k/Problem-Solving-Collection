"""Given a number N, the task is to find the largest prime factor of that number.

Example 1:

Input:
N = 5
Output:
5
Explanation:
5 has 1 prime factor 
i.e 5 only.

"""


def isprime(n):
    import math

    if n == 0 or n == 1:
        return False
    a = int(math.sqrt(n))
    for i in range(2, a + 1):
        if n % i == 0:
            return False
    return True


N = 24
factors = []
for i in range(1, N + 1):
    if N % i == 0 and isprime(i):
        factors.append(i)
print(max(factors))
