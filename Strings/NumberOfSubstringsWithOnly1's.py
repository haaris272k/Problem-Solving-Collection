"""Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s."""

# Logic Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.
# To get the consecutive ones just split the stirng into groups of consecutive 1s. In that case 0 will get removed automatically.
# then we can find the count of 1's and put in the formuala (c*(c+1))//2


s = "11001"

formula = 0

to_lst = s.split("0")

mod = 10 ** 9 + 7

for i in to_lst:

    c = i.count("1")

    formula += (c * (c + 1)) // 2

print(formula % mod)
