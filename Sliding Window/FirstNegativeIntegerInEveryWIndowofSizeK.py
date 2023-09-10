"""Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

 

Example 1:

Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6"""


from collections import deque


A = [-8, 2, 3, -6, 10]
K = 2

# declarations
start, end = 0, 0
N = len(A)
negativeQueue = deque()
answer = []

while end < N:
    # if we encounter a negative number, add it to the queue
    if A[end] < 0:
        negativeQueue.appendleft(A[end])
    # if the window size is equal to K then,
    # if the queue is empty that means there is no negative number in the window so,
    # we add 0 to the answer
    # else we add the first negative number in the queue to the answer
    # and we check if the first negative number in the queue is the same as the
    # first element in the window, if it is, we pop it from the queue
    if end - start + 1 == K:
        if negativeQueue:
            answer.append(negativeQueue[0])
            if A[start] == negativeQueue[0]:
                negativeQueue.popleft()
        else:
            # if the queue is empty, we add 0 to the answer
            answer.append(0)
        start += 1

    end += 1
print(answer)
