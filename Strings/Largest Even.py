"""Given a string and it contains the digits as well as non-digits.
We have to find the largest even number from available digits after removing the duplicates.
If not possible, print -1.

Sample Testcases :

I/P 1:
%#32%#%2
O/P 1:
32

I/P 2:
%#2373#@
O/P 2:
732"""


s = input("Enter the string ")
lst = []
for i in s:
    if i not in lst and i.isdigit():
        lst.append(i)
maximizing = sorted(lst, reverse=True)
to_int = int("".join(maximizing))
if to_int % 2 == 0:
    print(to_int)
else:
    print("-1")
