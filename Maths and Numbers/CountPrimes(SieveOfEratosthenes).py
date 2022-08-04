"""Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7."""

# -------------------------------------------------------------------------------#
# Naive solution
# O (N sqrt(N))
# TLE
import math


def prime(n):
    if n == 0 or n == 1:
        return False
    a = int(math.sqrt(n))
    for i in range(2, a + 1):
        if n % i == 0:
            return False
    return True


def countPrimes(n):
    count = 0
    for i in range(n):
        if prime(i):
            count += 1
    return count


n = 10
print(countPrimes(n))

# -------------------------------------------------------------------------------#

# Using Sieve algorithm (Eratosthenes)
# O(N log log N)


def Sieve(n):

    """Step 1: Edge cases"""
    # if n < 2, return 0
    if n == 0 or n == 1:
        return 0

    """Step 2: create a boolean table of size n"""
    primes = [True] * n
    # 0 and 1 are not prime so we set them to False in our table
    primes[0], primes[1] = False, False

    """Step 3: iterate through the boolean table and mark all non-prime numbers as False"""
    a = int(math.sqrt(n))
    # iterate from 2 to sqrt(n) (=a)
    for i in range(2, a + 1):
        # if i is prime, then mark all multiples of i as non-prime
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    """Step 4: Finding those prime numbers"""
    primes_numbers = []
    for a, b in enumerate(primes):
        if b:
            primes_numbers.append(a)

    print(primes_numbers)
    return sum(primes)


n = 10
print(Sieve(n))
