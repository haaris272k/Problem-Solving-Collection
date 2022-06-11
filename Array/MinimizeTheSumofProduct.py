"""You are given two arrays, A and B, of equal size N. The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] +…+ A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed.


Example 1:

Input:
N = 3 
A[] = {3, 1, 1}
B[] = {6, 5, 4}
Output:
23 
Explanation:
1*6+1*5+3*4 = 6+5+12
= 23 is the minimum sum"""


a = [6, 1, 9, 5, 4]
b = [3, 4, 8, 2, 4]
a.sort()  # sort one array in ascending order
b.sort(reverse=True)  # sort the other array in descending order
sum = 0
for i in range(len(a)):
    sum += a[i] * b[i]
print(sum)
