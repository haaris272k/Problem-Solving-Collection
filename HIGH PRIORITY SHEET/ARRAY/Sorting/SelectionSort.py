# Selction Sort O(n^2)
# O(1)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        swap(arr, i, min_idx)

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

print(selection_sort(arr))
