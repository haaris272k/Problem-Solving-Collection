"""Given an NxN matrix Mat. Sort all elements of the matrix."""
Mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]

temp = []
for i in Mat:
    for j in i:
        temp.append(j)
temp.sort()
temp = temp[::-1]

for i in range(len(Mat)):
    for j in range(len(Mat[0])):
        Mat[i][j] = temp.pop()

print(Mat)
