"""Find the Euler Totient Function (ETF) Φ(N) for an input N. 
ETF is the count of numbers in {1, 2, 3, …, N} that are relatively prime to N, i.e.,
the numbers whose GCD (Greatest Common Divisor) with N is 1."""


# Brute force method
# TLE
import math

N = 16
c_ = 0
for i in range(1, N + 1):
    GCD = math.gcd(i, N)
    if GCD == 1:
        c_ += 1
print(c_)
