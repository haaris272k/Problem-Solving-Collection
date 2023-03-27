# Merge sort
# Uses Divide and Conquer
# Time complexity: O(nlogn)
# Space Complexity:O(n)


def merge(left, right):  # Function to merge sorted lists
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lst):  # Function to sort a list
    if len(lst) <= 1:  # If list has only 1 element or is empty
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


print(merge_sort([1, 9, 1, 22, 10, 0, -1, -222222]))