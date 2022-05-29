"""Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'."""


s = "RLRRLLRLRL"
balance = 0
count = 0

# decreasing the value of 'balance' by 1 if the current character is L and increasing
# it by 1 if the current character is R
# as sson as the 'balance' will be 0 it means that the string is balanced so in order to
# count the number of times the string is balanced we need to increment the count variable

for i in range(len(s)):
    if s[i] == "L":
        balance -= 1
        print(balance)
    else:
        balance += 1
        print(balance)
    if balance == 0:
        count += 1
print(count)
