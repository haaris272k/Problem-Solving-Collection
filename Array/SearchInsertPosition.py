"""Given a sorted array Arr[](0-index based) consisting of N distinct integers and an integer k, the task is to find the index of k, if it’s present in the array Arr[]. Otherwise, find the index where k must be inserted to keep the array sorted.


Example 1:

Input:
N = 4
Arr = {1 , 3, 5, 6}
k = 5
Output: 2
Explaination: Since 5 is found at index 2 
as arr[2] = 5, the output is 2.
"""
N = 4
Arr = [1, 3, 5, 6]
k = 2
for i in range(N):
    if k == Arr[i]:
        print(i)
        break
else:
    Arr.append(k)
    Arr.sort()
    print(Arr.index(k))
