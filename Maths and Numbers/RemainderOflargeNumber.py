"""Program to find remainder when large number is divided by 11"""
"""Input : str = 13589234356546756
Output : 6"""

"""Note: You are not allowed to use any built-in function or type casting in this program."""


large_num = 1011
to_str = str(large_num)
length = len(to_str)
remainder = 0

for i in range(0, length):
    number = remainder * 10 + int(to_str[i])
    remainder = number % 11
print(remainder)
