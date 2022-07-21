"""Given an array arr[] of N positive integers. Push all the zeros of the given array to the right end of the array while maitaining the order of non-zero elements.


Example 1:

Input:
N = 5
Arr[] = {3, 5, 0, 0, 4}
Output: 3 5 4 0 0
Explanation: The non-zero elements"""

# TC: O(N)
# SC: O(N)
arr = [3, 5, 0, 0, 4]
NonZero = [i for i in arr if i != 0]
Zero = [i for i in arr if i == 0]
FinalArray = NonZero + Zero
print(FinalArray)

# TC: O(N)
# SC: O(1)
# Using zero as a pivot element and whenevever we find a non-zero element,
# we swap it with the pivot element.

length = len(arr)
pivot = 0
for i in range(length):
    if arr[i] != 0:
        arr[pivot], arr[i] = arr[i], arr[pivot]
        pivot += 1
