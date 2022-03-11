"""
A positive integer d is said to be a factor of another positive integer N if when N is divided by d, the remainder obtained is zero. For example, for number 12, there are 6 factors 1, 2, 3, 4, 6, 12. Every positive integer k has at least two factors, 1 and the number k itself.Given two positive integers N and k, write a program to print the kth largest factor of N.

Input Format: The input is a comma-separated list of positive integer pairs (N, k).

Output Format: The kth highest factor of N. If N does not have k factors, the output should be 1.

Example 1

    Input: 12,3
    Output: 4

"""


def problem(n, k):
    fact = []
    for i in range(1, n + 1):
        if n % i == 0:
            fact.append(i)
    print(fact)
    lar = []
    if len(fact) < k:
        return 1
    else:
        return fact[-k]


n, k = int(input("Enter the number: ")), int(
    input("Enter the kth max number you want to find: ")
)
print(problem(n, k))
