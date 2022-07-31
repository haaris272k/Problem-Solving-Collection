"""Given a string A. The string contains alphanumeric characters.
Find the sum of all numbers present in it.
A = "a12b34c"
output :46
"""
import re

# Method 1
str1 = "ab12cd34a1"
temp = "0"
s = 0
for i in str1:
    print(i)
    if i.isdigit():
        temp += i
        print("temp", temp)
    else:
        s += int(temp)
        print("s", s)
        temp = "0"
    final_sum = s + int(temp)
    print("final_sum", final_sum)
print(final_sum)

# Method 2 using regex
print(re.findall("\d+", str1))
print(sum(map(int, re.findall("\d+", str1))))
