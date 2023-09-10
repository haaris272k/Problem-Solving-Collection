"""Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4]."""

n = 5
list = []
for i in range(1, (n // 2) + 1):
    posi = i
    neg = -1 * i
    list.append(posi)
    list.append(neg)

if n % 2 != 0:
    list.append(0)
print(list)
