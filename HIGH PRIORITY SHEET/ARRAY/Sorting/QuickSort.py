def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []

        for idx, ele in enumerate(arr):
            if idx != 0 and ele <= pivot:
                less.append(ele)
            if ele > pivot:
                greater.append(ele)

    return quicksort(less) + [pivot] + quicksort(greater)


arr = [9, 2, 1, -1, 0, 10, 9]
print(quicksort(arr))
