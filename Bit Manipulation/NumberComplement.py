"""The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2."""


num = 5

""" Approach 1 using list for finding complement"""
# Converting the number to binary
to_bin = bin(num).replace("0b", "")

# converting to list of ints for easier manipulation to find complement
# Finding the complement of the number
to_lst = [int(i) for i in to_bin]
print(to_lst)
for i in range(len(to_lst)):
    if to_lst[i] == 1:
        to_lst[i] = 0
    else:
        to_lst[i] = 1
print(to_lst)
# converting back to string to find decimal value
to_str = "".join(str(i) for i in to_lst)

# Finding the decimal value of the complement
ans = int(to_str, 2)
print(ans)


"""Approach 2 using slicing to find complement"""
to_bin = bin(num).replace("0b", "")
for i in range(len(to_bin)):
    if to_bin[i] == "0":
        to_bin = to_bin[:i] + "1" + to_bin[i + 1 :]
    else:
        to_bin = to_bin[:i] + "0" + to_bin[i + 1 :]


to_dec = int(to_bin, 2)
print(to_dec)
