"""Given an array A of positive integers.
Your task is to find the leaders in the array.
An element of array is leader if it is greater than or
equal to all the elements to its right side. The rightmost element is always a leader. 


Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included."""


A = [16, 17, 4, 3, 5, 2]


leader = []
N = len(A)
# add the last element to the leader list as it is always a leader
leader.append(A[-1])

# start from the second last element and traverse the array in reverse order
for i in range(N - 2, -1, -1):
    if A[i] >= leader[-1]:
        leader.append(A[i])
print(leader)
