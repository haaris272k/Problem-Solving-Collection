"""ou are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]"""

# Algo
# (1) Transpose the matrix (reverse the matrix around the main diagonal)
# (2) reverse it from left to right (by using the property known as reflection)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(mat)


# tranpose (changing columns with rows and rows with columns)
for i in range(n):
    for j in range(i + 1, n):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
print(mat)

# reflection
for i in range(n):
    for j in range(n // 2):
        mat[i][j], mat[i][-j - 1] = mat[i][-j - 1], mat[i][j]

# print(mat)
