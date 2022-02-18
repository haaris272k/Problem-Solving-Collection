"""
Input: a string of comma separated numbers. The numbers 5 and 8 are present in the listAssume that 8 always comes after 5.

Case 1: num1 = add all numbers which do not lie between 5 and 8 in the input.
Case 2: num2= numbers formed by concatenating all numbers from 5 to 8.
Output: sum of num1 and num2

"""

# a = "3,2,6,5,1,4,8,9,8,8,3,6,7,6"
a = input()
b = a.split(",")
ind5 = b.index("5")
ind8 = b.index("8")
for_n2 = b[ind5 : ind8 + 1]
num2 = int("".join(for_n2))
for_n1 = []
for i in b:
    if i not in for_n2:
        for_n1.append(int(i))
num1 = sum(for_n1)
print(num1 + num2)
