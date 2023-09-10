# Using Recursion to find gcd of two numbers then find lcm of two numbers

# Formula for LCM of two numbers is (a * b) / gcd(a, b)

# Method 1
a, b = 15, 20


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


answer = a * b // gcd(a, b)

print(answer)

# Method 2 Using Inbuilt

GCD = gcd(a, b)
LCM = a * b // GCD

print(LCM)
