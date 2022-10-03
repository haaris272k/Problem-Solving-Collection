"""Given an array arr of distinct elements of size N, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]"""

arr = [1, 2, 3]

n = len(arr)


# [small,great,small,great]

# Method 1
# O(nlogn) and O(1)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


arr.sort()

for i in range(1, n - 1):
    swap(arr, i + 1, i)
print(arr)


# Method 2
#  O(n) and O(1)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


flag = True
for i in range(n - 1):
    if flag == True:
        if arr[i] > arr[i + 1]:
            swap(arr, i, i + 1)
    else:
        if arr[i] < arr[i + 1]:
            swap(arr, i, i + 1)
    flag = bool(1 - flag)
print(arr)
