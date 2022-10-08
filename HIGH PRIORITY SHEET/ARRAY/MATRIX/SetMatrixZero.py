"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]"""


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
r, c = len(matrix), len(matrix[0])

rows, columns = set(), set()


for i in range(r):
    for j in range(c):
        if matrix[i][j] == 0:
            rows.add(i)
            columns.add(j)
for i in range(r):
    for j in range(c):
        if i in rows or j in columns:
            matrix[i][j] = 0
print(matrix)
