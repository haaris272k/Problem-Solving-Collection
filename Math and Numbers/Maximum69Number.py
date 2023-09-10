"""You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969."""


# num = 9669
num = 9996
tolst = list(map(int, str(num)))
print(tolst)

for i in range(len(tolst)):
    currmax = num
    if tolst[i] == 6:
        tolst[i] = 9
        toint = int("".join(map(str, tolst)))
        if toint > currmax:
            currmax = toint
            break
print(currmax)
