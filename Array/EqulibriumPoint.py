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

# Approach 1: TC: O(n*n) SC: O(1)
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

# Approach 2: TC: O(n) SC: O(1)
# The idea is to get the total sum of the array first.
# Then Iterate through the array and keep updating the left sum which is initialized as zero
# In the loop, we can get the right sum by subtracting the elements one by one.


def equili(A):
    totalsum = sum(A)  # total sum of all elements
    leftsum = 0  # sum of elements from 0 to i
    for i in range(N):
        totalsum -= A[i]  # subtract the current element from total sum
        if leftsum == totalsum:
            return "YES"
        leftsum += A[i]
    return "NO"


print(equili(A))
