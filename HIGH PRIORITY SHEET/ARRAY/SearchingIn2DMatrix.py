"""Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x. Find whether element x is present in the matrix or not.

Example 1:

Input:
n = 3, m = 3, x = 62
matrix[][] = {{ 3, 30, 38},
              {36, 43, 60},
              {40, 51, 69}}
Output: 0
Explanation:
62 is not present in the matrix, 
so output is 0."""


def SearchIn2Dmatrix(matrix, x):
    for i in range(len(matrix)):
        if x in matrix[i]:
            return True
    return False


matrix = [[3, 30, 38], [36, 43, 60], [40, 51, 69]]
x = 69
print(SearchIn2Dmatrix(matrix, x))
