import collections

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
ans = []

""" 
Sliding Window + Brute Force
Time Complexity: O(nk)
Space Complexity: O(n-k+1) ~ O(n)

"""
start, end, n = 0, 0, len(arr)
while end < n:
    if end - start + 1 == k:
        subarr = arr[start : end + 1]
        ans.append(max(subarr))
        start += 1
    end += 1
print(ans)


""" 
Sliding Window + Deque
Time Complexity: O(n)
Space Complexity: O(n-k+1) ~ O(n)
"""
q = collections.deque()
while end < n:

    # make sure that queue is not empty and,
    # the last element of queue is less than the current element
    # (i.e the element we are inserting)
    while q and arr[end] > arr[q[-1]]:
        # pop smaller values from the queue
        q.pop()
    # add the current element to the queue
    # this is the index of the current element
    # not the value of the current element
    q.append(end)

    if start > q[0]:
        # remove the index of the element which is out of the window
        q.popleft()

    if end + 1 >= k:
        # add the maximum element of the current window
        ans.append(arr[q[0]])
        start += 1
    end += 1
print(ans)
