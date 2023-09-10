from heapq import heapify, heappop, heappush, heappushpop

"""Given an array Arr[] of size N and an integer K,
you have to choose the first two minimum elements of the array and erase them, then insert the sum of these two elements in the array until all the elements are greater than or equal to K and find the number of such operations required.

Example 1:

Input:
N = 6, K = 6 
Arr[] = {1, 10, 12, 9, 2, 3}
Output: 2
Explanation: First we add (1 + 2), now the
new list becomes 3 10 12 9 3, then we add
(3 + 3), now the new list becomes 6 10 12 9,
Now all the elements in the list are greater
than 6. Hence the output is 2 i:e 2 operations

are required to do this. """
arr = [5, 8]
k = 7

heapify(arr)

# choosing first two minimum elements from the heap and erase them
# pushing sum of them to the heap
# stop as soon as the minimum element is greater than equal to k
c = 0
while arr[0] < k and len(arr) > 1:
    a = heappop(arr)
    b = heappop(arr)
    heappush(arr, a + b)
    c += 1
if len(arr) == 1 and arr[0] < k:
    print(-1)
else:
    print(c)
