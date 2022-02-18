"""

WAP to determine whether a number N is equal to the sum of it's proper positive divisors (excluding the number itslef) 
Input:
3 (no of test cases)
6
5
28

Output:
Yes
No
Yes

"""

t = int(input("Enter test cases "))
for j in range(t):
    n = int(input("Enter num "))

    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print("Yes")
    else:
        print("No")
