"""Implement the Selection Sort algorithm"""

# TC : O(n^2)
def SelectionSort(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [1, 0, 4, 3, 12, 20]
n = len(arr)
print(SelectionSort(arr, n))
