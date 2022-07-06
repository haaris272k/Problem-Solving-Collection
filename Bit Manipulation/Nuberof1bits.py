"""'Write a function that takes an unsigned integer and returns the number of 
'1' bits it has (also known as the Hamming weight).

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011
has a total of three '1' bits.
"""
n = 00000000000000000000000000001011

# Brute force method (O(n)):
def numberOf1Bits(n):
    count = 0
    for i in range(len(n)):
        if n[i] == "1":
            count += 1
    return count


print(numberOf1Bits(n))

# Bit manipulation method (O(1)):
def numberOf1Bits(n):
    count = 0
    while n != 0:
        count += 1
        n = n & (n - 1)
    return count


print(numberOf1Bits(n))
