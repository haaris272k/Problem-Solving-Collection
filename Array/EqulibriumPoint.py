"""Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Note: Retun the index of Equilibrium point. (1-based index)

Example 1:

Input: 
n = 5 
A[] = {1,3,5,2,2} 
Output: 3 
Explanation: For second test case 
equilibrium point is at position 3 
as elements before it (1+3) = 
elements after it (2+2). """


A = [11, 12111, 3, 11]
N = len(A)
ind = []
if len(A) == 1:
    print(A[0])
for i in range(N):
    sum_left = sum(A[:i])
    sum_right = sum(A[i + 1 :])
    if (sum_left) == (sum_right):
        ind.append(i + 1)
if ind:
    print(ind[0])
else:
    print(False)
