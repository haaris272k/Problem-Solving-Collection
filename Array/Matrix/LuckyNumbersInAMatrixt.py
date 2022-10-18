"""Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column."""

# matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]

# Brute Force
row = len(matrix)
col = len(matrix[0])

for i in range(row):
    for j in range(col):
        min_row = min(matrix[i])
        max_col = max([matrix[k][j] for k in range(row)])
        if min_row == max_col:
            print(min_row)

# using mapp

min_max_row_column_map = {"row": [], "col": []}
for i in range(row):
    min_of_all_rows = min(matrix[i])
    min_max_row_column_map["row"].append(min_of_all_rows)
print(min_max_row_column_map)

for j in range(col):
    max_of_all_cols = max([matrix[k][j] for k in range(row)])
    min_max_row_column_map["col"].append(max_of_all_cols)

print(min_max_row_column_map)

for i in range(row):
    for j in range(col):
        if min_max_row_column_map["row"][i] == min_max_row_column_map["col"][j]:
            print(min_max_row_column_map["row"][i])
