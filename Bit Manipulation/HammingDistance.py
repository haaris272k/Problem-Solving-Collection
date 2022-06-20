"""The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""


"""
Hamming distance is a metric for comparing two binary data strings.
While comparing two binary strings of equal length, Hamming distance is 
the number of bit positions in which the two bits are different.
In order to calculate the Hamming distance between two strings, and ,
we perform their XOR operation, (a⊕ b), and then count the total number of 1s in the resultant string.
"""

x, y = 1, 4
print(bin(x ^ y).count("1"))
