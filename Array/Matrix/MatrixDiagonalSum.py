"""Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8"""

mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
left_diagnol_elements = []
right_diagnol_elements = []

# For left diagonal elements
# One pattern could be observed that the [element to be considered=index of the matrix]
# Means mat[i][i] has to be considered for the left diagnol elements

for i in range(len(mat)):

    left_diagnol_elements.append(mat[i][i])


# Same will be done for right diagonal elements
# It could be achieved by reversing the matrix and then taking the elements

for i in range(len(mat)):

    right_diagnol_elements.append(mat[i][::-1][i])

if len(mat) % 2 == 0:
    print(sum(left_diagnol_elements) + sum(right_diagnol_elements))
else:
    print(
        sum(left_diagnol_elements)
        + sum(right_diagnol_elements)
        - mat[len(mat) // 2][len(mat) // 2]
    )
