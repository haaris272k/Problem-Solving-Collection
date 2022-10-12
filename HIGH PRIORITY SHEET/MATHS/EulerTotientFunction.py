"""Find the Euler Totient Function (ETF) Φ(N) for an input N. 
ETF is the count of numbers in {1, 2, 3, …, N} that are relatively prime to N, i.e.,
the numbers whose GCD (Greatest Common Divisor) with N is 1."""

"""Euler’s Totient function Φ (n) for an input n is the count of numbers in {1, 2, 3, …, n-1} that are relatively prime to n, i.e., 
the numbers whose GCD (Greatest Common Divisor) with n is 1."""
# Brute force method
# TLE
# NlogN
import math

N = 16
c_ = 0
for i in range(1, N + 1):
    GCD = math.gcd(i, N)
    if GCD == 1:
        c_ += 1
print(c_)


"""Below is a Better Solution. The idea is based on Euler’s
product formula which states that the value of totient functions 
is below the product overall prime factors p of n. """


n = 16
result = n
p = 2
while p * p <= n:
    if n % p == 0:
        while n % p == 0:
            n = n // p
        result *= 1 - (1 / p)
p = p + 1

if n > 1:
    result *= 1 - (1 / n)

print(int(result))
