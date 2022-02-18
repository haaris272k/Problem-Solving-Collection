"""
Reverse a string after removing duplicate charcaters

input: google
output: elog

input: hello
output: oleh

"""

b = input()
lst = []
for i in b:
    if i not in lst:
        lst.append(i)
to_str = "".join(lst)
print(to_str[::-1])
