"""Given an integer array Arr of size N the task is to find the count of elements whose value is greater than all of its prior elements.

Note : 1st element of the array should be considered in the count of the result.

For example,
Arr[]={7,4,8,2,9}
As 7 is the first element, it will consider in the result.
8 and 9 are also the elements that are greater than all of its previous elements.
Since total of  3 elements is present in the array that meets the condition.
Hence the output = 3."""


arr = [7, 4, 8, 2, 9]
# arr = [5, 3, 4, 5, 8, 9]
count = 0

# O(n^2)
for i in range(len(arr)):
    if i != 0:
        ele = arr[i]
        for j in arr[:i]:
            if ele > j:
                count += 1
                break
print(count + 1)


# O(n)
for i in range(len(arr)):
    if i == 0 or arr[i] > arr[i - 1]:
        count += 1
print(count)
