"""Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.



 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]"""

matrix = [[1, 2, 3], [4, 5, 6]]
new_matrix = []
rows_len = len(matrix)  # length of rows
column_len = len(matrix[0])  # length of columns


# We have to take care of the fact the length of the rows and columns will get interchanged
# After transposing the matrix

for i in range(column_len):  # iterate over the columns

    new_matrix.append([])  # append a new row

    for j in range(rows_len):  # iterate over the rows

        new_matrix[i].append(matrix[j][i])

print(new_matrix)
