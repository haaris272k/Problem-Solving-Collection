"""

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample Output

0.500000
0.333333
0.166667


"""


def precision_problem(arr, len_arr):
    pos = []
    neg = []
    zero = []

    for i in range(len(arr)):
        if arr[i] >= 1:
            pos.append(arr[i])
        if arr[i] < 0:
            neg.append(arr[i])

        if arr[i] == 0:
            zero.append(arr[i])

    ratio_pos = len(pos) / len_arr
    ratio_negs = len(neg) / len_arr
    ratio_zeros = len(zero) / len_arr

    print("%.6f" % round(ratio_pos, 6))
    print("%.6f" % round(ratio_negs, 6))
    print("%.6f" % round(ratio_zeros, 6))
    return "Done"


arr = list(map(int, input().split()))
len_arr = len(arr)
print(precision_problem(arr, len_arr))
