"""The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2."""


num = 430043
newnum = str(num)
window = 2


start, end, count = 0, 0, 0
while end < len(newnum):
    if (end - start + 1) == window:
        number = int(newnum[start : end + 1])
        print(number)
        if number != 0 and num % number == 0:
            count += 1
        start += 1
        end += 1
    else:
        end += 1
print(count)
