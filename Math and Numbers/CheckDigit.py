"""
WAP to check for nix number.
A number is ninx if it contains digit '6' or '9'

input: 12345678
output: Yes

input: 19923
output: Yes

input: 12341
output: No

"""

n = int(input())
conv_s = str(n)
listB = [i for i in conv_s]
conv_s2 = listB
if "6" in conv_s2 or "9" in conv_s2:
    print("Yes")
else:
    print("No")
