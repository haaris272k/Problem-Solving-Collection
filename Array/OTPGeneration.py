""" 
Input will be like this 5624381275. separate odd places integers and return 4-digit OTP by squaring the digits

input: 1234567890
(24680=> separating odd placed integers
41636640=> squaring them 
4163=> returning first 4 digits)
output: 4163

"""

b = int(input())
a = str(b)
l1 = []
l2 = []
for i in range(len((a))):
    if i % 2 != 0:
        l1.append(int(a[i]) * int(a[i]))
l2 = [str(j) for j in l1]
s = "".join(l2)
print(s[0:4])
